from table import Table


class Playfair(Table):
    """
    Классовая реализация шифра Плейфера

    :param key: Ключ закрытого алфавита
    """
    def __init__(self, key: str) -> str:
        key = self.replace(key)
        print(key)
        if self.check_bad_lang(key): 
            print("Должны использоваться исключительно русские символы!")
            del self
            return
        key = self.edit_key(key)
        self.alph = self.make_alph(key)

    def crypt_b(self, bigr: str) -> str:
        """
        Функция шифрования биграмм

        :param bigr: Шифруемая биграмма
        :returns: Зашифрованная биграмма
        """
        nums = [[self.alph.index(bigr[0]) // 5, self.alph.index(bigr[0]) % 5],
                [self.alph.index(bigr[1]) // 5, self.alph.index(bigr[1]) % 5]]
        """Массив для хранения строк и столбцов символов биграммы"""
        if nums[0][0] == nums[1][0]:
            # Проверяем, совпадают ли строки
            # Если да, то прибавляем к столбцу единицу
            nums[0][1] = (nums[0][1] + 1) % 5
            nums[1][1] = (nums[1][1] + 1) % 5
        elif nums[0][1] == nums[1][1]:
            # Проверяем совпадают ли столбцы
            # Если да, то прибавляем к строке единицу
            nums[0][0] = (nums[0][0] + 1) % 5
            nums[1][0] = (nums[1][0] + 1) % 5
        else:
            # Иначе взаимозаменяем номера столбцов
            t = nums[0][1]
            nums[0][1] = nums[1][1]
            nums[1][1] = t
        bigr = "".join([self.alph[nums[0][0] * 5 + nums[0][1]], self.alph[nums[1][0] * 5 + nums[1][1]]])
        return bigr
    
    def decrypt_b(self, bigr: str) -> str:
        """
        Функция расшифрования биграмм

        :param bigr: Расшифруемая биграмма
        :returns: Расшифрованная биграмма
        """
        nums = [[self.alph.index(bigr[0]) // 5, self.alph.index(bigr[0]) % 5],
                [self.alph.index(bigr[1]) // 5, self.alph.index(bigr[1]) % 5]]
        if nums[0][0] == nums[1][0]:
            # Проверяем, совпадают ли строки
            # Если да, то отнимаем от столбца единицу
            nums[0][1] = (5 + nums[0][1] - 1) % 5
            nums[1][1] = (5 + nums[1][1] - 1) % 5
        elif nums[0][1] == nums[1][1]:
            # Проверяем совпадают ли столбцы
            # Если да, то отнимаем от строки единицу
            nums[0][0] = (5 + nums[0][0] - 1) % 5
            nums[1][0] = (5 + nums[1][0] - 1) % 5
        else:
            # Иначе взаимозаменяем номера столбцов
            t = nums[0][1]
            nums[0][1] = nums[1][1]
            nums[1][1] = t
        bigr = "".join([self.alph[nums[0][0] * 5 + nums[0][1]], self.alph[nums[1][0] * 5 + nums[1][1]]])
        return bigr

    def crypt(self, text: str) -> str:
        """
        Функция шифрования текста

        :param text: Шифруемый текст
        :returns: Зашифрованный текст
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
    
    def decrypt(self, text: str) -> str:
        """
        Функция расшифрования текста

        :param text: Зашифрованный текст
        :returns: Расшифрованный текст
        """
        ctext = ""
        while len(ctext) < len(text):
            ctext += self.decrypt_b(text[len(ctext)] + text[len(ctext) + 1])
        return ctext