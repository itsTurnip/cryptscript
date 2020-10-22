from abc import abstractmethod, ABC

class Table(ABC):
    """
    Общий класс для квадратных шифров.
    Некоторые особенности: 
        Используется алфавит в 30 символов для построения таблицы 
        без использования лишних символов
        ё = е, й = и, ъ = ь
    """

    """Алфавит открытого текста"""
    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
    
    @staticmethod    
    def replace(x: str) -> str:
        """
        Функция замены измененных в алфавите символов

        :param x: Строка, в которой заменяем символы
        :returns: Измененная строка.
        """
        x = x.strip().lower()
        table = x.maketrans("ёйъ", "еиь", "!()-[]{};:'\",<>./?@#$%^&*_~\n ")
        return x.translate(table)
    
    def check_bad_lang(self, *args: str) -> bool:
        """
        Функция проверки строк на отсутствие символов в алфавите

        :param args: Строки для проверки
        :returns: True, если отсутствующие символы присутствуют, иначе False.
        """
        for x in args:
            for sym in x:
                if sym not in self.alphabet:
                    return True
        return False

    @staticmethod
    def edit_key(key: str) -> str:
        """
        Изменяем ключ, исключая повторяющиеся символы

        :param key: Изменяемый ключ
        :returns: Измененный ключ
        """
        newkey = ""
        for sym in key:
            if sym not in newkey:
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
            if sym not in alph:
                alph += sym
        return alph
    
    def decrypt(self, ctext: str) -> str:
        """
        Функция расшифрования текста

        :param ctext: расшифруемый текст
        :returns: расшифрованный текст
        """
        text = ""
        length = len(text)
        while length < len(ctext):
            text += self.decrypt_b(ctext[length:length+2])
            length = len(text)
        return text

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
            ctext += self.crypt_b(text[length:length + 2])
            length = len(ctext)
        return ctext

    @abstractmethod
    def crypt_b(self, bigr: str) -> str:
        """
        Метод для шифрования биграмм.

        :param bigr: шифруемая биграмма
        :returns: зашифрованная биграмма
        """
        pass

    @abstractmethod
    def decrypt_b(self, bigr: str) -> str:
        """
        Метод для расшифрования биграмм.

        :param bigr: расшифруемая биграмма
        :returns: расшифрованная биграмма
        """
        pass
