string = input('Введите слова (через пробел): ')
vowel = 'ауоыиэяюёе'
consonant ='бвгджзйклмнпрстфхцчшщ'
count_cons = count_vow = 0

for i in range(len(string)):
    if string[i] in consonant:
        count_cons += 1
    if string[i] in vowel:
        count_vow += 1
print('Количество согласных букв: ', count_cons, 'Количество гласных букв: ', count_vow)