# Библиотека colorama нужна для вывода цветного текста в терминале,
# чтобы делать вывод сообщения удобным для чтения

from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + "SUCCESS: Все установлено и работает стабильно.")
print(Fore.YELLOW + "WARNING: BUG ALERT")
print(Fore.RED + "ERROR: Something went wrong.")
print(Style.BRIGHT + "BRIGHT: Bright text without color")