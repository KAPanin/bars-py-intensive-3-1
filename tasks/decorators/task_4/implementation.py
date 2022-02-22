from time import sleep
from tasks.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                try:
                    result = func(*args, **kwargs)
                except AssertionError:
                    pass

                if result:
                    break
                sleep(delay)
            else:
                raise MyException

            return result
        return wrapper
    return decorator


