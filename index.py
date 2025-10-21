# ТАК РАБОТАТЬ НЕ БУДЕТ, Т.К. ПЕРЕМЕНАЯ file ОБЪЯВЛЕНА ТОЛЬКО В БЛОКЕ try, В finally НЕ ДОСТУПНА!
# try:
#     file = open('text.txt', 'r') #+ 'r' ( read ) - не создаёт не существ. файл, только читать

#     file.read()

    
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     file.close() #+ пишу сдесь, т.к. в try ошибка срабатывает на 1-й строке, а дальше код не пойдёт!

#! ТАК БУДЕТ РАБОТАТЬ, С МЕНЕДЖЕРОМ "With ... as":
try:
    with open("data/text.txt", "r", encoding="utf-8") as file: #+ Этот менеджер сам открывает и сам закрывает файл!
        print(file.read())
except FileNotFoundError:
    print("Файл не найден")
