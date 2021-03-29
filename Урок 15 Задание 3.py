
def Complex(n):
    if n <= 1 or n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False



x = int(input('Введите число: '))
if Complex(x):
    print('Число {} - составное'.format(x))
else:
    print('Число {} - простое'.format(x))
