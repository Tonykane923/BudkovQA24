import random

# Указываем диапазон для программы
number = (int(random.uniform(1, 500)))
# Число попыток угадывания
count = 1
# Пользователь вводит число
player = int(input("Угадай число от 1 до 500: "))
# Начинаем цикл
while player != number:
    # Увеличиваем счетчик попыток
    count += 1
    # Если число больше
    if player > number:
        player = int(input("Не угадал, ваше число слишком большое, попробуйте еще раз: "))
    # Если число меньше
    elif number > player > 0:
        player = int(input("Не угадал, ваше число слишком маленькое, попробуйте еще раз: "))
    # Выход из игры
    elif player == 0:
        print("Увидимся в следующий раз")
        break
# Если угадал
if player == number: print("Поздравляю. Вы угадали число под номером", player, "всего", count, "попыток")
