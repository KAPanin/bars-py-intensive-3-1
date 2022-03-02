from ..models import *
from django.db.models import Count, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """

    order_in_date = Order.objects.filter(date_formation__range=(begin, end))

    customer_order = order_in_date.values_list(
        'customer__name',
    ).annotate(
        dcount=Count('id'),
        min_date=Min('date_formation'),
    ).order_by(
        '-dcount',
        'min_date',
        'customer__name',
    )

    return customer_order.values_list('customer__name', 'dcount').first()
