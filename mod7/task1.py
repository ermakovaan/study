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


@validate_args
def example_function(num: int) -> str:
    """
    Пример функции, которая использует декоратор для валидации аргументов.

    Args:
    - num: Передаваемый аргумент.

    Returns:
    - str: Сообщение об успешной валидации или сообщение об ошибке.

    """
    return f"The argument {num} is valid."


if __name__ == '__main__':
    print(example_function(5))              # Вывод: The argument 5 is valid.
    print(example_function())               # Вывод: Not enough arguments
    print(example_function(10, 15))   # Вывод: Too many arguments
    print(example_function("hello"))        # Вывод: Wrong types
    print(example_function(-3))             # Вывод: Negative argument
