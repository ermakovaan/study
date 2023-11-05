def generator():
    i = 11
    while True:
        digits_x = [int(x) for x in str(i)]
        digits_y = len(digits_x)
        arms_sum = sum([x ** digits_y for x in digits_x])
        if arms_sum == i:
            yield i
        i += 1

armstrong = generator()
def get_armstrong_numbers():
    return next(armstrong)

for i in range(8):
    print(get_armstrong_numbers(), end=" ")