# Пользователь вводит строку
x = input("Введите строку: ")
# Пользователь указвает нужный символ, который указал выше
y = input("Введите искомый символ: ")
x = list(x)

# Расчитываем количество
kolichestvo = len([i for i in x if i == y])
print("Символ встречается", kolichestvo, "раз(а)")
