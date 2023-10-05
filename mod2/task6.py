domain = input('Введите имя сайта: ')
dom1 = dom2 = dom3 = ''
count = 0

for i in domain:
    if i == '.':
        count += 1
    else:
        if count == 0:
            dom3 += i
        elif count == 1:
            dom2 += i
        elif count == 2:
            dom1 += i

print(dom1)
print(dom2)
print(dom3)