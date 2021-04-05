a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
d = int(input('Введите число: '))


def max4(a, b, c, d):
    return max(max(max(a, b), c), d)


print(max4(a, b, c, d))
