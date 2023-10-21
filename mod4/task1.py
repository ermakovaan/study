numbers_list = input("Введите несколько чисел через пробел: ").split ()
def check_numbers(numbers):
    if len(set(numbers)) == 1:
        print("Все числа равны")
    elif len(set(numbers)) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")
check_numbers(numbers_list)
