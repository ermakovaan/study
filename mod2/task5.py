number = input('Введите символ и целое число: ')
x = number[:1]
y = int(number[2:])
leter = 'abcdefghijklmnopqrstuvwxyz'
index = 0

for z in range(len(leter)):
    if leter[z] == x:
        index = (z + y) % len(leter)

print(leter[index])