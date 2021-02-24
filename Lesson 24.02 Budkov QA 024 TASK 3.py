x = int(input("Ведите первое число: "))
y = int(input("Ведите второе число: "))
z = int(input("Ведите третье число: "))
d = int(input("Ведите четвертое число: "))

largest_number = x
if y > largest_number:
    largest_number = y
if z > largest_number:
    largest_number = z
if d > largest_number:
    largest_number = d
print("Наибольшее число:", largest_number)
