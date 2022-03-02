from ..models import *
from django.db.models import Sum, F


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """

    # Проверка на время заказа
    order_in_date = OrderItem.objects.filter(
        order__date_formation__range=(begin, end)
    )

    # Проверка количества товара
    order_item_with_enough_count = order_in_date.filter(
        order__date_formation__range=(
            F('product__productcount__begin'),
            F('product__productcount__end')
        ),
        count__lte=F('product__productcount__value')
    )

    # Если товара хватает, то берем столько, сколько указано в заказе
    # Если не хватает, то берем весь товар, что есть
    if order_item_with_enough_count.exists():
        count_from = 'count'
    else:
        order_item_with_enough_count = order_in_date.filter(
            order__date_formation__range=(
                F('product__productcount__begin'),
                F('product__productcount__end')
            )
        )
        count_from = 'product__productcount__value'

    # Считаем общее количество товара по всем заказам
    product_list = order_item_with_enough_count.values_list(
        'product__name',
    ).annotate(
        count=Sum(count_from),
    ).order_by(
        '-count',
    )

    max_product = []
    _cost = None
    for product, cost in product_list.iterator():

        if _cost is None:
            _cost = cost

        if _cost == cost:
            max_product.append((product, int(cost)))
        else:
            break

    return max_product
