from ..models import *
from django.db.models import Sum, F


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    order_in_date = OrderItem.objects.filter(order__date_formation__range=(begin, end))

    product_list = order_in_date.values_list(
        'product__name',
    ).annotate(
        count=Sum('count'),
    ).order_by(
        '-count',
    )

    max_product = []
    _cost = 0
    for product, cost in product_list.iterator():
        if _cost != cost and not _cost:
            _cost = cost
            max_product.append((product, int(cost)))
        else:
            break

    return max_product
