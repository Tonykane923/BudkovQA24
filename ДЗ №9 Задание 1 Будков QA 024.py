# Вводим первую границу диапазона
x = int(input("Введите первую границу (меньшую): "))
# Вводим вторую границу диапазона
y = int(input("Введите вторую границу (большую): "))
# Вводим число
z = int(input("Введите любое число: "))

# Начинаем цикл

for i in range(x, y + 1):

    # Пишем условие, если число не попадет в диапазон, чтобы пользователь ввел число еще раз

    while z > y or z < x:
        z = int(input("Введите число повторно: "))

    # Выводим диапазон и выделяем введенное число восклицательным знаком

    if i == z:
        print(" ! ", i, " ! ", end=" ")
    else:
        print(i, end=",")

# Не пойму как убрать запятую после последнего числа (вконце диапазона) для косметического эффекта