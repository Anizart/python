# try:
#     x = int(input("Введите число: "))
#     x += 5
#     print(x)
# except ValueError: #+ Отслеживаю ошибку ValueError
#     print("Введите число")

def get_input():
    x = int(input("Введите число (x): "))
    y = int(input("Введите число (y): "))
    return [x, y]

x = 0
while x == 0:
    try:
        list = get_input()
        [x, y] = list
        res = x / y
        print(round(res))
        break
    except ValueError:
        print("Введите число")
        x = 0
    except  ZeroDivisionError:
        print("Деление на 0. Решения нет")
        x = 0
    finally:
        print("finally")