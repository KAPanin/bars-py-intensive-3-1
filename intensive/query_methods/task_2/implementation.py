from ..models import *
from django.db.models import Count, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    order_in_date = Order.objects.filter(date_formation__lte=end, date_formation__gte=begin)

    if order_in_date.exists():

        result_customer = order_in_date.values_list('customer__name').\
            annotate(dcount=Count('customer'), min_date=Min('date_formation')).\
            order_by('-dcount', 'min_date', 'customer__name')

        return result_customer.values_list('customer__name', 'dcount')[0]
