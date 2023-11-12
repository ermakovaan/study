import time

def validate_args(function):
    def pack(*args, **kwar):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"

        if not isinstance(args[0], int):
            return "Wrong types"

        if args[0] < 0:
            return "Negative argument"

        return function(*args, **kwar)

    return pack

class Timer:
    def __init__(self, function):
        self.function = function
        self.start = None
        self.end = None

    def __call__(self, *args, **kwar):
        if self.start is None:
            self.start = time.time()
            result = self.function(*args, **kwar)
            self.end = time.time()
            print(f"Функция {self.function.__name__!r} выполнялась {(self.end - self.start):.4f} секунд")
            self.start = None
            self.end = None
        else:
            result = self.function(*args, **kwar)
        return result


def memoize(function):
    buffer = dict()

    def memoized_function(*args):
        if args in buffer:
            return buffer[args]
        result = function(*args)
        buffer[args] = result
        return result

    memoized_function.__name__ = function.__name__
    memoized_function.__doc__ = function.__doc__
    return memoized_function


@validate_args
@Timer
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30)) 


@Timer
def fibonacci_no_memoize(n):
    if n < 2:
        return n
    return fibonacci_no_memoize(n - 1) + fibonacci_no_memoize(n - 2)

print(fibonacci_no_memoize(30)) 