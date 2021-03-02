a = int(input ('Введите месяц: '))                           ## Пользователю нужно ввести месяц от 1 до 12
if a == 1 or a == 2 or a == 12:                              ## Условие для зимы
    print ('Winter')
elif a == 3 or a == 4 or a == 5:
    print ('Spring')                                         ## Условие для весны
elif a == 6 or a == 7 or a == 8:
    print ('Summer')                                         ## Условие для лета
elif a == 9 or a == 10 or a == 11:
    print ('Autumn')                                         ## Условие для осени
else:
    print ('ОШИБКА!!!!!')                                    ## Если пользователь ввел чмсло вне диапазона