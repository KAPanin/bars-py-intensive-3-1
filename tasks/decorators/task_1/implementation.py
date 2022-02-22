import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнеия функции:  {time.time() - start_time}")
        return result

    return wrapper
