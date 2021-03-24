import random
diapason = []
even = []
odd = []
negative = []
positive = []
listeven = [random.randint(-100, 100) for diapason in range(20) if diapason % 2 == 0]
listodd = [random.randint(-100, 100) for diapason in range(20) if diapason % 2 != 0]

print(listeven)
print(listodd)
