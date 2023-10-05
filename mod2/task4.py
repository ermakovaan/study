x = x1 = x2 = int(input('Введите натуральное число: '))
binary = octal = hex = ''
figure = "0123456789ABCDEF"

if x > 0:
    while x > 0:
        binary = figure[x % 2] + binary
        x //= 2
    while x1 > 0:
        octal = figure[x1 % 8] + octal
        x1 //= 8
    while x2 > 0:
        hex = figure[x2 % 16] + hex
        x2 //= 16
    print(binary, octal, hex)
else:
    print('Неверный ввод')