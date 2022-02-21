from datetime import datetime, date


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    date_ = {
        'y': some_date.year,
        'm': some_date.month,
        'd': some_date.day
    }
    
    if is_last_day_in_month(date_['d'], date_['m'], date_['y']):
        if date_['m'] == 12:
            date_['y'] = date_['y'] + 1
            date_['m'] = 1
        else:
            date_['m'] = date_['m'] + 1
        date_['d'] = 1
    else:
        date_['d'] = date_['d'] + 1

    return date(year=date_['y'], month=date_['m'], day=date_['d'])


def is_last_day_in_month(day, month, year):
    if day == 31 and month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    if day == 30 and month in [4, 6, 9, 11]:
        return True
    if month == 2 and (day == 29 or (day == 28 and year % 4 != 0)):
        return True
    return False
