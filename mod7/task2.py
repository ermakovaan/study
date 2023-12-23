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


@memoize
def fibonacci(n: int) -> int:
    """
    Рекурсивная функция для вычисления чисел Фибоначчи.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
