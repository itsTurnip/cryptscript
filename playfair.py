from .table import Table

class Playfair(Table):
    """
    Классовая реализация шифра Плейфера

    :param key: Ключ закрытого алфавита
    """

    def __init__(self, key: str) -> str:
        key = self.replace(key)
        if self.check_bad_lang(key): 
            raise ValueError("Должны использоваться исключительно русские символы!")
        key = self.edit_key(key)
        self.alph = self.make_alph(key)

    def crypt(self, text: str) -> str:
        """
        Функция шифрования текста

        :param text: шифруемый текст
        :returns: зашифрованный текст
        """
        text = self.replace(text)
        if self.check_bad_lang(text):
            raise ValueError()
        if len(text) % 2 == 1:
            text += 'ь'
        ctext = ""
        length = len(ctext)
        while length < len(text):
            if text[length] == text[length+1]:
                text = text[:length+1] + 'ьь' + text[length+1:]
            ctext += self.crypt_b(text[length:length + 2])
            length = len(ctext)
        return ctext
    
    def crypt_b(self, bigr: str) -> str:
        """
        Функция шифрования биграмм

        :param bigr: Шифруемая биграмма
        :returns: Зашифрованная биграмма
        """
        first_x, first_y = self.alph.index(bigr[0]) // 5, self.alph.index(bigr[0]) % 5
        second_x, second_y = self.alph.index(bigr[1]) // 5, self.alph.index(bigr[1]) % 5
        """Массив для хранения строк и столбцов символов биграммы"""
        if first_x == second_x:
            # Проверяем, совпадают ли строки
            # Если да, то прибавляем к столбцу единицу
            first_y = (first_y + 1) % 5
            second_y = (second_y + 1) % 5
        elif first_y == second_y:
            # Проверяем совпадают ли столбцы
            # Если да, то прибавляем к строке единицу
            first_x = (first_x + 1) % 6
            second_x = (second_x + 1) % 6
        else:
            # Иначе взаимозаменяем номера столбцов
            first_y, second_y = second_y, first_y
        bigr = self.alph[first_x * 5 + first_y] + self.alph[second_x * 5 + second_y]
        return bigr
    
    def decrypt_b(self, bigr: str) -> str:
        """
        Функция расшифрования биграмм

        :param bigr: Расшифруемая биграмма
        :returns: Расшифрованная биграмма
        """
        first_x, first_y = self.alph.index(bigr[0]) // 5, self.alph.index(bigr[0]) % 5
        second_x, second_y = self.alph.index(bigr[1]) // 5, self.alph.index(bigr[1]) % 5
        if first_x == second_x:
            # Проверяем, совпадают ли строки
            # Если да, то отнимаем от столбца единицу
            first_y = (first_y - 1) % 5
            second_y = (second_y - 1) % 5
        elif first_y == second_y:
            # Проверяем совпадают ли столбцы
            # Если да, то отнимаем от строки единицу
            first_x = (first_x - 1) % 6
            second_x = (second_x - 1) % 6
        else:
            # Иначе взаимозаменяем номера столбцов
            first_y, second_y = second_y, first_y
        bigr = self.alph[first_x * 5 + first_y] + self.alph[second_x * 5 + second_y]
        return bigr

    def decrypt(self, text: str) -> str:
        """
        Функция расшифрования текста

        :param text: Зашифрованный текст
        :returns: Расшифрованный текст
        """
        ctext = ""
        while len(ctext) < len(text):
            ctext += self.decrypt_b(text[len(ctext):len(ctext) + 2])
        return ctext
