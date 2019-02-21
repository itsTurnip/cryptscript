# cryptscript
Набор различных реализаций шифров.

Описание файлов:

* table - наследуемый класс для квадратных шифров
* playfair - шифр Плейфера (квадрат Плейфера)
* wheat - шифр Уитстона (шифр двойного квадрата)
* fourtable - шифр четырёх квадратов

Использование:

```python
from cryptscript import Wheat
from cryptscript import Playfair

# Инициализация класса шифрования с ключами "энциклопедия" "трусости", 
# которые будут использованы для шифрования
wheat = Wheat("энциклопедия", "трусости")

opentext = "Жил бы цитрус в чащах юга?"
crypttext = wheat.crypt(opentext)
decrypttext = wheat.decrypt(crypttext)


playfair = Playfair("Колбаса")

opentext = "Жил бы цитрус в чащах юга?"
crypttext = playfair.crypt(opentext)
decrypttext = playfair.decrypt(crypttext)

```
