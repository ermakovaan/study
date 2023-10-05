number = input('Введите число в строку (из 0 и 1): ')
x = y = 0

for i in number:
    if i == '0':
        x += 1
    if i == '1':
        y += 1

if y == x:
    print('yes')
else:
    print('no')