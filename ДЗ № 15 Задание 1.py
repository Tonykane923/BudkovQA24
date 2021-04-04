length = int(input("Введите сторону квадрата: "))
symbol = input("Введите символ: ")
occupancy = input("Введите заполняемость, 1 - заполненный квадрат, 2 - не заполненный: ")
if occupancy == "1":
    zug = True
else:
    zug = False


def draw_square(length, symbol, occupancy):
    r = symbol * length
    if not occupancy:
        m = symbol + " " * (length - 2) + symbol
    else:
        m = r
    print(r)
    for i in range(length - 2):
        print(m)

    print(r)


draw_square(length, symbol, True)

draw_square(length, symbol, False)
# Тут есть очевидная ошибка почему он рисует всё сразу, но до меня не доходит