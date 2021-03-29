a = int(input("Введите первый параметр: "))
b = int(input("Введите второй параметр: "))


def odd_seq(a, n=1):
    if n <= a:
        print(n, end=' ')
        odd_seq(a, n + 2)
    else:
        return


odd_seq(100)