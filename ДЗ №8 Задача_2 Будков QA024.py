    # Пользователь вводит число
data = int(input("Число: "))
# ВВодим условия для чисел меньше 0 и пока чсило не равно семи
while data != 7:
    if data < 0:
        print("Number is negative")

# Условия для чисел больше нуля
    elif data > 0:
        print("Number is positive")

# Условия, если число равно нулю
    elif data == 0:
        print("Number is equal to zero")

    data = int(input("Число: "))
print( "Good bye!")


