from ..models import *
from django.db.models import Sum, F, Q
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
    order_in_date = OrderItem.objects.filter(order__date_formation__lte=end,
                                             order__date_formation__gte=begin)

    result = Decimal(0)

    if order_in_date.exists():
        join_table = order_in_date.select_related('product_count'). \
            filter(Q(order__date_formation__lte=F('product__productcost__end')) &
                   Q(order__date_formation__gte=F('product__productcost__begin')))

        without_product = join_table.exclude(product__name=product)

        order_cost = list(without_product.values('order__number'). \
            annotate(cost=Sum(F('count') * F('product__productcost__value'))). \
            values_list('cost', flat=True))

        if len(order_cost) > 0:
            result = sum(order_cost) / len(order_cost)

    return result
