str_and_char = input('Введите строку и символ (через запятую): ')
i = counter = 0
string = char = ''
for j in str_and_char:
    if j == ',':
        string = str_and_char[:counter]
        char = str_and_char[counter + 1:]
        break
    counter += 1
while string[i] == char:
    counter += 1
    i += 1
print(i)

