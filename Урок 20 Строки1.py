line = input("Ведите строку: ")

new_line = []

new_string = ' '
for i in range(len(line), 0, -1):
    new_line.append(line[i - 1])
for i in new_line:
    new_string += i


print(new_string)