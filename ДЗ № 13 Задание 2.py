# Пользователь вводит арифметическую операцию: сложение, вычитание, умножение или деление
line = input("Введите арифметическое выражение: ")

i = 0
# Вводим первый аргумент и пишем цикл
arg1 = []
while True:
    if line[i] in '1234567890':
        arg1.append(line[i])
        i += 1
    else:
        break
arg1 = int(''.join(arg1))

if line[i] not in '+-/*':
    raise ValueError
op = line[i]
i += 1
# Вводим второй аргумент и пишем цикл
arg2 = []
while True:
    try:
        if line[i] in '1234567890':
            arg2.append(line[i])
            i += 1
    except IndexError:
        break
arg2 = int(''.join(arg2))

print(arg1, op, arg2)
# Для сложения
if op == '+':
    print(arg1 + arg2)
# Для вычитания
elif op == '-':
    print(arg1 - arg2)
# Для умножения
elif op == '*':
    print(arg1 * arg2)
# Для деления
elif op == '/':
    print(arg1 - arg2)