flowers = []
x = int(input('Введите количество видов цветов минимум 4: '))
for i in range(x):
    flowers.append(input('Введите названия цветов по одному за ввод: '))
bouquet = input('Введите количество этих цветов в букете: ')

lst = [item for item in flowers if item in bouquet]

if not lst:
    print("Название второго по встречаемости вида:",  )
else:
    print(f'Название вида, цветы которого встречаются в букете чаще всего{", ".join(lst)}.')