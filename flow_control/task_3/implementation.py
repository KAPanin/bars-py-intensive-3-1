from datetime import datetime


def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    count_day = 0
    if month in ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']:
        count_day = 31
    elif month in ['апрель', 'июнь', 'сентябрь', 'ноябрь']:
        count_day = 30
    elif month == 'февраль':
        if datetime.now().year % 4 == 0:
            count_day = 29
        else:
            count_day = 28

    return count_day
