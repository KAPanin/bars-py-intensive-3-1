from ..models import *
from django.db.models import Sum, F, Count
from decimal import (
    Decimal,
)


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """

    order_without_product = OrderItem.objects.values_list(
        'order_id',
        flat=True
    ).filter(
        product__name=product
    )

    order_in_date = OrderItem.objects.filter(
        order__date_formation__range=(begin, end)
    ).exclude(
        order__in=order_without_product
    )

    order_with_price = order_in_date.filter(
        order__date_formation__range=(
            F('product__productcost__begin'),
            F('product__productcost__end')
        )
    )

    order_cost = order_with_price.values_list(
        'order__number'
    ).aggregate(
        cost=Sum(F('count') * F('product__productcost__value')),
        count=Count('order__number', distinct=True)
    )

    if order_cost['count']:
        result = order_cost['cost'] / order_cost['count']
    else:
        result = Decimal(0)

    return result
