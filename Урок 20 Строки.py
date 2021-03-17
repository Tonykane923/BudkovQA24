stroka = [1, 2, 3, 4, 5, 6]
new_stroka = []

index = len(stroka) - 1

while index >= 0:
    item = stroka[index]
    new_stroka.append(item)

    index -= 1

print(new_stroka)