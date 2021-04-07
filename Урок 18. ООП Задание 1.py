sec = int(input("Введите количество секунд: "))
minutes = int(input("Введите количество минут: "))
hours = int(input("Введите количество часов: "))


def time(minutes, hours):
    x = minutes * 60
    y = hours * 3600


print("Общее количество секунд: ", x + y + sec)
time(minutes, sec)
