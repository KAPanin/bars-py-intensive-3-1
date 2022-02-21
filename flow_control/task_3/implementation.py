from datetime import datetime


def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    if month in ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']:
        return 31
    elif month in ['апрель', 'июнь', 'сентябрь', 'ноябрь']:
        return 30
    elif month == 'февраль':
        if datetime.now().year % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 0
