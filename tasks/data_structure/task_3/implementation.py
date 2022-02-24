def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает копию словаря.
    """
    return {key: get_new_value(value) for key, value in origin_dict.items()}


def copy_list(origin_list: list) -> list:
    """
    Функция возвращает копию списка.
    """
    return [get_new_value(value) for value in origin_list]


def copy_tuple(origin_tuple: tuple) -> tuple:
    """
    Функция возвращает копию списка.
    """
    return tuple(get_new_value(value) for value in origin_tuple)


def get_new_value(value):
    """
    Функция создающая копию элемента, если это dict, list или tuple
    """
    if type(value) == dict:
        new_value = copy_dict(value)
    elif type(value) == list:
        new_value = copy_list(value)
    elif type(value) == tuple:
        new_value = copy_tuple(value)
    else:
        new_value = value

    return new_value
