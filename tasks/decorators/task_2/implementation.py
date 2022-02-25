from tasks.common import MyException
from tasks.decorators.task_1.implementation import time_execution
from tasks.common import factorial


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):
        if type(arg) == int and arg >= 0:
            return func(arg)
        else:
            raise MyException

    return wrapper


def cache(func):
    """
    Обертка, которая кэширует результат
    """
    saved_cache = {}

    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if not saved_cache.get(cache_key):
            saved_cache[cache_key] = func(*args, **kwargs)
        return saved_cache[cache_key]

    return wrapper


new_factorial = cache(factorial)
new_factorial = time_execution(new_factorial)

new_factorial(100000)  # Время выполнеия функции:  2.2102606296539307
new_factorial(100000)  # Время выполнеия функции:  6.67572021484375e-06
