## Пользователь вводит два числа: первое < второго
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
i = 0
for i in range(x,y):
    if (i & 1) != 0:
        print(i)
