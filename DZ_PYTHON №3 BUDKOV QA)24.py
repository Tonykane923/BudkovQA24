prof_one = input('Введите свою профессию\n')
prof_two = input('Введите свою профессию\n')
prof_three = input('Введите свою профессию\n')
prof_one1 = input('Чем разделить?\n')
prof_two2 = input('Чем разделить?\n')

print(f'Кто он?\nОн - {prof_one} {prof_one1} {prof_two} {prof_two2}  {prof_three}')
print('========================================================')
minutes = int(input("Введите кол-во минут: "))
a = (minutes//60) % 60
b = minutes % 60
print(""+str(a)+"часа(ов) и "+str(b)+" минут")