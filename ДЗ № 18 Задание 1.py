list = input("Введите строку: ")

symbol = input("Введите символ: ")

count = 0

for i in list:

    if i == symbol:
        count += 1

position = list.index(symbol)

print("Символ встречается: ", count, "раз(а)")

print("Первый раз на позиции: ", position + 1)
