number = input('Введите делимое и делитель (через запятую и пробел): ')
number_1 = 0
number_2 = 0
score = 0
for i in number:
    if i == ',':
        number_1 = int(number[:score])
        number_2 = int(number[score + 2:])
    score += 1
print(number_1 % number_2)