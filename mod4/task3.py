def nod(x, y):
    while(y):
        x, x = y, x % y
        return x
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
numbers = nod(x, y)
print("НОД двух чисел равен:", numbers)