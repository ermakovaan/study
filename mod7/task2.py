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

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)