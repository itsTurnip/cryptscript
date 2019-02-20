from table import Table


class Wheat(Table):
    """
    Классовая реализация шифра Уитстона (шифр двойного квадрата)

    :param k1: Первая часть ключа, используется в первой таблице
    :param k2: Вторая часть ключа, используется во второй таблице
    """
    def __init__(self, k1: str, k2: str):
        k1, k2 = map(self.replace, [k1, k2])
        if self.check_bad_lang(k1, k2):
            print("Должны использоваться исключительно русские символы!")
            del self
            return
        k1, k2 = self.edit_key(k1), self.edit_key(k2)
        self.alph1, self.alph2 = self.make_alph(k1), self.make_alph(k2)

    def crypt_b(self, bigr: str) -> str:
        """
        Функция шифрования (расшифрования) биграмм

        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        nums = [[self.alph1.index(bigr[0]) // 5, self.alph1.index(bigr[0]) % 5],
                [self.alph2.index(bigr[1]) // 5, self.alph2.index(bigr[1]) % 5]]
        """Массив для хранения строк и столбцов символов биграммы"""
        # Проверяем, совпадают ли столбцы
        if nums[0][1] == nums[1][1]:
            # Если да, меняем строки
            t = nums[0][0]
            nums[0][0] = nums[1][0]
            nums[1][0] = t
        else:
            # Иначе взаимозаменяем номера столбцов
            t = nums[0][1]
            nums[0][1] = nums[1][1]
            nums[1][1] = t
        # Формируем зашифрованную биграмму
        bigr = "".join([self.alph1[nums[0][0] * 5 + nums[0][1]], self.alph2[nums[1][0] * 5 + nums[1][1]]])
        return bigr

    def crypt(self, text: str) -> str:
        """
        Функция шифрования (расшифрования) текста

        :param text: шифруемый текст
        :returns: зашифрованный текст
        """
        text = self.replace(text)
        if self.check_bad_lang(text):
            print("Допускается использовать только русский алфавит!")
            return
        if len(text) % 2 == 1:
            text += "ь"
        ctext = ""
        while len(ctext) < len(text):
            ctext += self.crypt_b(text[len(ctext)] + text[len(ctext) + 1])
        return ctext

    """Алиас для расшифрования текста"""
    decrypt = crypt
    """Алиас для расшифрования биграмм"""
    decrypt_b = crypt_b
