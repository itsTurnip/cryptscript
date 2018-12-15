class table():
    """
    Общий класс для квадратных шифров.
    Некоторые особенности: 
		Используется алфавит в 30 символов для построения таблицы 
		без использования лишних символов
		ё = е, й = и, ъ = ь
    """

    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
    """Алфавит открытого текста"""
    
    def replace(self, x: str) -> str:
        """
		Функция замены измененных в алфавите символов

		:param x: Строка, в которой заменяем символы
		:returns: Измененная строка.
        TODO:
		* Избавиться от кучи replace
		"""
        return x.lower().replace(" ", "").replace("ё", "е").replace("й", "и").replace("ъ", "ь")

    def check_bad_lang(self, *args: str) -> bool:
    	"""
		Функция проверки строк на отсутствие символов в алфавите

		:param args: Строки для проверки
        :returns: True, если отсутствующие символы присутствуют, иначе False.
		"""
    	for x in args:
    		for sym in x:
    			if not sym in self.alphabet:
    				return True
    	return False
		
    def edit_key(self, key: str) -> str:
    	"""
		Изменяем ключи, исключая повторяющиеся символы

		:param key: Изменяемый ключ
		:returns: Измененный ключ
		"""
    	newkey = ""
    	for sym in key:
    		if not sym in newkey:
    			newkey += sym
    	return newkey
	
    def make_alph(self, key: str) -> str:
    	"""
    	Функция создания закрытого алфавита

    	:param key: Ключ для алфавита
    	:returns: Закрытый алфавит
    	"""
    	alph = key
    	for sym in self.alphabet:
    		if not sym in alph:
    			alph += sym
    	return alph