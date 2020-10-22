from .table import Table


class Four(Table):
    """
    Классовая реализация шифра четырех квадратов.

    :param k1: Первая часть ключа, используется в первой таблице
    :param k2: Вторая часть ключа, используется во второй таблице
    """
    def __init__(self, k1: str, k2: str):
        k1, k2 = map(self.replace, [k1, k2])
        if self.check_bad_lang(k1, k2):
            raise ValueError("Должны использоваться исключительно русские символы!")
        k1, k2 = self.edit_key(k1), self.edit_key(k2)
        self.alph1, self.alph2 = self.make_alph(k1), self.make_alph(k2)

    def crypt_b(self, bigr: str) -> str:
        """
        Функция шифрования биграмм

        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        first_x, first_y = self.alphabet.index(bigr[0]) // 5, self.alphabet.index(bigr[0]) % 5
        second_x, second_y = self.alphabet.index(bigr[1]) // 5, self.alphabet.index(bigr[1]) % 5
        # Меняем столбцы местами
        first_y, second_y = second_y, first_y
        return self.alph1[first_x * 5 + first_y] + self.alph2[second_x * 5 + second_y]

    def decrypt_b(self, bigr: str) -> str:
        """
        Фунция расшифрования биграмм

        :param bigr: биграмма для расшифрования
        :return: расшифрованная биграмма
        """
        first_x, first_y = self.alph1.index(bigr[0]) // 5, self.alph1.index(bigr[0]) % 5
        second_x, second_y = self.alph2.index(bigr[1]) // 5, self.alph2.index(bigr[1]) % 5
        """Массив для хранения строк и столбцов символов биграммы"""
        # Меняем столбцы местами
        first_y, second_y = second_y, first_y
        return self.alphabet[first_x * 5 + first_y] + self.alphabet[second_x * 5 + second_y]
