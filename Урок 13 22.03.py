from random import randint

x = int(input('Введите размер списка: '))
numbers = []
for i in range(x + 1):
    numbers.append(randint(-100, 100))
list.sort(numbers)
print('Минимальное значение: ', numbers[0])
list.reverse((numbers))
print('Максимальное значение: ', numbers[0])
y = len([j for j in numbers if j<0])
print('Количество отрицательных чисел: ', y)
z = len([j for j in numbers if j>0])
print('Количество положительных чисел: ', y)
g = len([j for j in numbers if j == 0])
print("Количество нулей: ", g)