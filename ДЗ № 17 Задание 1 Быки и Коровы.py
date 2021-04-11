import random


# Возвращаем список введенных чисел

def getDigits(num):
    return [int(i) for i in str(num)]


# Возвращаем TRUE, если число не имеет дублирующих чисел, иначе FALSE

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


# Генерируем четырехзначное число без повторяющихся цифр
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

# Возвращаем общие цифры в том порядке, в котором их ввели для быков и общие для коров

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):

        if j in num_li:

            if j == i:
                bull_cow[0] += 1

            else:
                bull_cow[1] += 1

    return bull_cow

# Тут пользователь вводит число
num = generateNum()
tries = int(input('Введите количество попыток: '))
# Я не понял как вывести количество попыток вконце, поэтому ввел еще один параметр и после выведу его

# Напишем цикл, с условием, где не будет одинаковых цифр в числе
while tries > 0:
    guess = int(input("Введите ваше число: "))

    if not noDuplicates(guess):
        print("Чичло не должно содержать одинаковых цифр")
        continue
    if guess < 1000 or guess > 9999:
        print("Введите четырехзначное число еще раз")
        continue

    bull_cow = numOfBullsCows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1

    if bull_cow[0] == 4:
        print("ВЫ УГАДАЛИ!!!")
        break
else:
    print(f"Ваши попытки закончились. Загаданное число {num}")
print("Количество попыток: ", tries)
