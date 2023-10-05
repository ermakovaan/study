number = input('Введите три числа от -1000 до 1000 (через пробел): ')
a = b = c = ''
space_count = 0
for i in number:
    if i == ' ':
        space_count += 1
    else:
        if space_count == 0:
            a += i
        elif space_count == 1:
            b += i
        elif space_count == 2:
            c += i

a = int(a)
b = int(b)
c = int(c)

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(b)