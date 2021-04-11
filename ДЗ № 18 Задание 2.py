line = input("Введите строку: ")

final = []

for i in line:
    if i != " ":
        final.append(i)
        final.append(".")
    else:
        final.append(" ")
print("Итог:", " ".join(final))


print("========================================================")
# Есть другой вариант

line = input("Введите строку: ")
final = ''
j = 1
for i in line:
    final += i
    j += 1
print('. '.join(list(final)))
