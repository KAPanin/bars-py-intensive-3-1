def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    
    if is_last_day_in_month(some_date.day, some_date.month, some_date.year):
        if some_date.month == 12:
            result_date = some_date.replace(year=some_date.year + 1, month=1, day=1)
        else:
            result_date = some_date.replace(month=some_date.month + 1, day=1)
    else:
        result_date = some_date.replace(day=some_date.day + 1)

    return result_date


def is_last_day_in_month(day, month, year):
    return any([day == 31 and month in [1, 3, 5, 7, 8, 10, 12],
                day == 30 and month in [4, 6, 9, 11],
                month == 2 and (day == 29 or (day == 28 and year % 4 != 0))])
