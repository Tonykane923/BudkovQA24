list = []
num = input("Введите список чисел: ") # В ДЗ в этой строчке.split(',') Но так не рабоатет
for i in num:
    if i != " ":
        list.append(i)


def bubble_sort(list):
    perestanovka_on = True
    while perestanovka_on:
        perestanovka_on = False
        for i in range(len(list) - 1):
            if int(list[i]) > int(list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                perestanovka_on = True
    print("Отсортировано пузырьком:", list)


bubble_sort(list)


def sort(list):
    list.sort()
    print("Отсортировано встроенным методом Питон:", list)

sort(list)
