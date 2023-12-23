def get_armstrong_numbers():
    """
    Генератор для чисел Армстронга.
    """
    number = 10
    while True:
        digits = [int(digit) for digit in str(number)]
        power = len(digits)
        armstrong_sum = sum(digit ** power for digit in digits)
        if armstrong_sum == number:
            yield number
        number += 1


if __name__ == "__main__":
    armstrong_gen = get_armstrong_numbers()
    for i in range(8):
        print(next(armstrong_gen), end=' ')
