code = input('Введите код: ')

sum_odd = 0
for i in range(0, len(code), 2):
    sum_odd += int(code[i])

sum_even = 0
for i in range(1, len(code), 2):
    sum_even += int(code[i])

if (sum_odd + 3 * sum_even) % 10 == 0:
    print('yes')
else:
    print('no')
