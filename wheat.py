from .table import Table


class Wheat(Table):
    """
    Классовая реализация шифра Уитстона (шифр двойного квадрата)

    :param k1: Первая часть ключа, используется в первой таблице
    :param k2: Вторая часть ключа, используется во второй таблице
    """
    def __init__(self, k1: str, k2: str):
        k1, k2 = map(self.replace, [k1, k2])
        if self.check_bad_lang(k1, k2):
            raise ValueError("Должны использоваться только русские символы в качетсве ключей")
        k1, k2 = self.edit_key(k1), self.edit_key(k2)
        self.alph1, self.alph2 = self.make_alph(k1), self.make_alph(k2)

    def crypt_b(self, bigr: str) -> str:
        """
        Функция шифрования биграмм

        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        first_x, first_y = self.alph1.index(bigr[0]) // 5, self.alph1.index(bigr[0]) % 5
        second_x, second_y = self.alph2.index(bigr[1]) // 5, self.alph2.index(bigr[1]) % 5
        # Проверяем, совпадают ли строки
        if first_x == second_x:
            # Если да, взаимозаменяем номера столбцов, буквы берём из тех же таблиц, где находились исходные
            first_y, second_y = second_y, first_x
            return self.alph1[first_x * 5 + first_y] + self.alph2[second_x * 5 + second_y]
        else:
            # Иначе взаимозаменяем номера столбцов, буквы биграммы берём из разных таблиц
            first_y, second_y = second_y, first_y
            return self.alph2[first_x * 5 + first_y] + self.alph1[second_x * 5 + second_y]
    
    def decrypt_b(self, bigr: str) -> str:
        """
        Функция для расшифрования биграмм
        
        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        # Сразу вычислим координаты так, как если бы у нас произошла замена из разных таблиц
        first_x, first_y = self.alph2.index(bigr[0]) // 5, self.alph2.index(bigr[0]) % 5
        second_x, second_y = self.alph1.index(bigr[1]) // 5, self.alph1.index(bigr[1]) % 5
        # Поскольку номера строк у нас сохраняются, следует для начала проверить, не одинаковы ли они.
        if first_x == second_x:
            # Строки равны, значит, буквы брались из исходных таблиц. Просчитаем столбцы, сразу же их заменив
            first_y, second_y = self.alph2.index(bigr[1]), self.alph1.index(bigr[0])
            return self.alph1[first_x * 5 + first_y] + self.alph2[second_x * 5 + second_y]
        else:
            # Если нет, то заменяем столбцы
            first_y, second_y = second_y, first_y
            return self.alph1[first_x * 5 + first_y] + self.alph2[second_x * 5 + second_y]
