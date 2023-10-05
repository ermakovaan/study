number = input('Введите номер телефона: ')
result = ''
rig_brac = ')'
lef_brac = '('
dash = '-'
space = ' '
for i in number:
    if i != space and i != rig_brac and i != lef_brac and i != dash:
        result += i
print(result)

