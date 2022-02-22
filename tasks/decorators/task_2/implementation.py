from tasks.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):
        if isinstance(arg, int) and arg >= 0:
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
