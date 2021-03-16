# Вводим диапазон
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
for i in range(num1, num2 + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        print(i, end=' ')