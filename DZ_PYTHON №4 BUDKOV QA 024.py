metres = float(input("Ведите количество метров: "))
centimetres = metres * 100.0
decimeters = metres * 10.0
millimeters = metres * 1000.0
miles = metres * 0.000621371
print("Вы получили сантиметров:", centimetres, "Вы получили дециметров:", decimeters,
      "Вы получили милиметров:", millimeters, "Вы получили миль:", miles)
print('===================================================================================')
a = input("Введите четырехзначное число:\n")
b = a[::-1]
print(b)

