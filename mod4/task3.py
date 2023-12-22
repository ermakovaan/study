def nod(x, y):
    (more, less) = (max(x, y), min(x, y))
    if more % less == 0:
        return less
    else:
        return nod(less, more % less)

x, y = map(int, input("Введите два числа через пробел: ").split(" "))
print("НОД двух чисел равен:", nod(x, y))