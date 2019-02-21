<<<<<<< HEAD
from .table import Table
=======
from table import Table
>>>>>>> refs/remotes/origin/master


class Four(Table):
    """
    Классовая реализация шифра четырех квадратов.

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
        Функция шифрования биграмм

        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        nums = [[self.alphabet.index(bigr[0]) // 5, self.alphabet.index(bigr[0]) % 5],
                [self.alphabet.index(bigr[1]) // 5, self.alphabet.index(bigr[1]) % 5]]
        """Массив для хранения строк и столбцов символов биграммы"""
        # Меняем столбцы местами
        t = nums[0][1]
        nums[0][1] = nums[1][1]
        nums[1][1] = t
        # Формируем зашифрованную биграмму
        bigr = "".join([self.alph1[nums[0][0] * 5 + nums[0][1]], self.alph2[nums[1][0] * 5 + nums[1][1]]])
        return bigr

    def crypt(self, text: str) -> str:
        """
        Функция шифрования текста

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

    def decrypt_b(self, bigr: str) -> str:
        """
        Фунция расшифрования биграмм

        :param bigr: биграмма для расшифрования
        :return: расшифрованная биграмма
        """
        nums = [[self.alph1.index(bigr[0]) // 5, self.alph1.index(bigr[0]) % 5],
                [self.alph2.index(bigr[1]) // 5, self.alph2.index(bigr[1]) % 5]]
        """Массив для хранения строк и столбцов символов биграммы"""
        # Меняем столбцы местами
        t = nums[0][1]
        nums[0][1] = nums[1][1]
        nums[1][1] = t
        # Формируем зашифрованную биграмму
        bigr = "".join([self.alphabet[nums[0][0] * 5 + nums[0][1]], self.alphabet[nums[1][0] * 5 + nums[1][1]]])
        return bigr

    def decrypt(self, text: str) -> str:
        """
        Функция расшифрования текста

        :param text: шифруемый текст
        :returns: зашифрованный текст
        """
        ctext = ""
        while len(ctext) < len(text):
            ctext += self.decrypt_b(text[len(ctext)] + text[len(ctext) + 1])
        return ctext
