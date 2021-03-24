# Введите строку для проверке палиндрома
с = input("Введите строку: ")
l = len(с)
l = l // 2
for i in range(l):
    # Разворачиваем строку
    if с[i] != с[-1 - i]:
        print("It's not palindrome")
        break
else:
    print("It's palindrome")
input()
