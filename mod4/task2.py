def function(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return function(a ** 2, n / 2)
    else:
        return a * function(a, n - 1)

a, n = map(int, input("Введите число и в какую степень его возвести: ").split(" "))
print(function(a, n))

