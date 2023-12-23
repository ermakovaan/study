import time


def memoize(func: callable) -> callable:
    """
    Декоратор, реализующий мемоизацию для функций.
    Мемоизация - сохранение результатов выполнения функций для ускорения последующих вызовов с теми же аргументами.

    Args:
    - func: Функция, для которой применяется мемоизация.

    Returns:
    - wrapper: Обертка, выполняющая мемоизацию для переданной функции.
    """
    cache = {}

    def wrapper(*args: int) -> int:
        """
        Функция-обертка, выполняющая мемоизацию для переданной функции.

        Args:
        - args: Аргументы, переданные в функцию.

        Returns:
        - Результат выполнения функции для заданных аргументов.
        """
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


def validate_args(func: callable) -> callable:
    def wrapper(*args: int) -> str:
        """
        Декоратор для валидации аргументов функции.

        Args:
        - args: Передаваемые аргументы функции.

        Returns:
        - str: Сообщение об ошибке, если аргументы не соответствуют заданным условиям, или результат выполнения функции.

        """
        if len(args) != 1:
            if len(args) < 1:
                return "Not enough arguments"
            else:
                return "Too many arguments"

        if not isinstance(args[0], int):
            return "Wrong types"

        if args[0] < 0:
            return "Negative argument"

        return func(*args)

    return wrapper


def timer_decorator(func: callable) -> callable:
    """
    Декоратор, который измеряет время выполнения функции.

    Args:
    - func: Функция, время выполнения которой измеряется.

    Returns:
    - wrapper: Обертка, измеряющая время выполнения функции.
    """

    class Timer:
        def __init__(self, function: callable):
            self.function = function
            self.start = None
            self.end = None

        def __call__(self, *args: any, **kwargs: any) -> any:
            """
            Выполняет замер времени выполнения функции.

            Args:
            - args: Позиционные аргументы функции.
            - kwargs: Именованные аргументы функции.

            Returns:
            - result: Результат выполнения функции.
            """
            if self.start is None:
                self.start = time.time()
                result = self.function(*args, **kwargs)
                self.end = time.time()
                print(f"{(self.end - self.start):.4f} секунд")
                self.start = None
                self.end = None
            else:
                result = self.function(*args, **kwargs)
            return result

    return Timer(func)


@validate_args
@timer_decorator
@memoize
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer_decorator
def fibonacci_without_memoize(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_without_memoize(n - 1) + fibonacci_without_memoize(n - 2)


if __name__ == '__main__':
    number_for_test = 35

    print("fibonacci с использованием memoize выполнялась: ", end='')
    fibonacci(number_for_test)

    print("fibonacci без использования memoize выполнялась: ", end='')
    fibonacci_without_memoize(number_for_test)
