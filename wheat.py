class wheat():
	"""
	Классовая реализация шифра Уитстона (шифр двойного квадрата)
	
	Некоторые особенности: 
		Используется алфавит в 30 символов для построения таблицы 
		без использования лишних символов
		ё = е, й = и, ъ = ь
	"""
	alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
	
	def __init__(self, k1, k2):
		"""
		k1 - первая часть ключа, используется в первой таблице
		k2 - вторая часть ключа, используется во второй таблице
		"""
		k1, k2 = map(self.replace, [k1, k2])
		if self.check_bad_lang(k1, k2): 
			print("Должны использоваться исключительно русские символы!")
			return
		k1, k2 = self.edit_keys(k1), self.edit_keys(k2)
		self.alph1, self.alph2 = self.make_alph(k1), self.make_alph(k2)
		
	def replace(self, x):
		"""
		Функция замены измененных в алфавите символов
		TODO:
			* Избавиться от кучи replace
		Аргументы:
			x (str): строка, в которой заменяем символы
		Возвращаемое значение:
			str: измененная строка.
		"""
		return x.lower().replace(" ", "").replace("ё", "е").replace("й", "и").replace("ъ", "ь")
	
	def check_bad_lang(self, *args):
		"""
		Функция проверки строк на отсутствие символов в алфавите
		Аргументы:
			args (str): строки для проверки
		Возвращаемое значение:
			bool: True, если отсутствующие символы присутствуют, иначе False.
		"""
		for x in args:
			for sym in x:
				if not sym in self.alphabet:
					return True
		return False
			
	def edit_keys(self, key):
		"""
		Изменяем ключи, исключая повторяющиеся символы
		Аргументы:
			key (str): изменяемый ключ
		Возвращаемое значение:
			str: измененный ключ
		"""
		newkey = ""
		for sym in key:
			if not sym in newkey:
				newkey += sym
		return newkey
	
	def make_alph(self, key):
		"""
		Функция создания закрытого алфавита
		Аргументы:
			key (str): ключ для алфавита
		Возвращаемое значение:
			str: закрытый алфавит
		"""
		alph = key
		for sym in self.alphabet:
			if not sym in alph:
				alph += sym
		return alph
	
	def crypt_b(self, bigr):
		"""
		Функция шифрования (расшифрования) биграмм
		Аргументы:
			bigr (str): шифруемая биграмма
		Возвращаемое значение:
			str: зашифрованная биграмма
		"""
		nums = [] # Массив для хранения номеров строк и столбцов символов биграммы в таблице закрытых алфавитов
		nums.append([self.alph1.index(bigr[0]) // 5, self.alph1.index(bigr[0]) % 5])
		nums.append([self.alph2.index(bigr[1]) // 5, self.alph2.index(bigr[1]) % 5])
		# Проверяем, совпадают ли столбцы
		if nums[0][1] == nums[1][1]:
			# Если да, меняем строки
			t = nums[0][0]
			nums[0][0] = nums[1][0]
			nums[1][0] = t
		else:
			# Иначе меняем столбцы
			t = nums[0][1]
			nums[0][1] = nums[1][1]
			nums[1][1] = t
		# Формируем зашифрованную биграмму
		bigr = "".join([self.alph1[nums[0][0] * 5 + nums[0][1]], self.alph2[nums[1][0] * 5 + nums[1][1]]])
		return bigr
		
	def crypt(self, text):
		"""
		Функция шифрования (расшифрования) текста
		Аргументы:
			text (str): шифруемый текст
		Возвращаемое значение:
			str: зашифрованный текст
		"""
		text = self.replace(text)
		if self.check_bad_lang(text):
			print("Допускается использовать только русский алфавит!")
			return
		if len(text) % 2 == 1: text += "ь"
		ctext = ""
		while len(ctext) < len(text):
			ctext += self.crypt_b(text[len(ctext)] + text[len(ctext) + 1])
		return ctext
