import random
diapason = []
even = []
odd = []
negative = []
positive = []
for i in range(20):
    i = random.randint(-100, 100)
    diapason.append(i)
for j in diapason:
    if j % 2 == 0:
        even.append(j)
    elif j % 2 == 1:
        odd.append(j)
for j in diapason:
    if j < 0:
        negative.append(j)
    elif j > 0:
        positive.append(j)
print("Чётные числа: ", even)
print("Нечётные числа: ", odd)
print("Меньше нуля: ", negative)
print("Больше нуля: ", positive)
