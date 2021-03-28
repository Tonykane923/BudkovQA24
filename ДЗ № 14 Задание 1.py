import random

# Заполняем список случайными числами
# Создаем списки
spisok1 = []
spisok2 = []
List1 = []  # Список для элементов обоих списков
List2 = []  # Список для элементов обоих списков без повторений
List3 = []  # Список для общих элементов
List4 = []  # Список для уникальных элементов
List5 = []  # Список для максимальных и минимальныъ элементов

# Задаём длину списков

for i in range(20):
    elem1 = random.randint(0, 100)
    spisok1.append(elem1)
    elem2 = random.randint(0, 100)
    spisok2.append(elem2)
    if elem1 == elem2:
        # Добавляем в список все одинаковые числа
        List3.append(elem1)
        # доюовляем в список все одинаковые числа но без повторений
        List2.append(elem1)
    if elem1 != elem2:
        List4.append(elem1)
    if elem2 != elem1:
        List4.append(elem2)

# Создаём общий список
List1.append(spisok1)
List1.append(spisok2)
# Создаём список общих элементов
List5.append(min(spisok1))
List5.append(min(spisok2))
List5.append(max(spisok1))
List5.append(max(spisok2))

print("Первый рандомный список", spisok1)

print("Второй рандомный список", spisok2)

print("Общий список", List1)

print("Список с общими числами", List3)

print("Список с числами без повторений", List2)

print("Список с уникальными числами", List4)

print("Минимальные и максимальные значения из двух списков", List5)

