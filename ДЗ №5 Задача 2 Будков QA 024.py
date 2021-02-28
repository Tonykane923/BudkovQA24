metres = float(input("Ведите количество метров: "))
Inches = metres * 39.370
Yards = metres * 1.0936
Miles = metres * 0.000621371
выбор = input("Мили, Дюймы или Ярды: ")
if выбор == "Мили":
    print("Вы получили миль = ",float(metres * 0.000621371))
if выбор == "Дюймы":
    print("Вы получили дюймов = ",float(metres * 39.370))
if выбор == "Ярды":
    print("Вы получили ярдов = ", float(metres * 1.0936))
