# Вводится строка
line = input("Введите строку: ")
# Вводится слово для поиска, которое хотите заменить
word = input("Введите слово для поиска: ")
# Вводится слово, которое будет заменой
some_new_word = input("Введите слово для замены: ")
# Делаем цикл и ищем слово для замены
for i in range(len(line) - len(word) + 1):
    if word == line[i:i + len(word)]:
        line = line.replace(word, some_new_word)
    
print(line)
