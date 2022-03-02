from ..models import *
from django.db.models import Sum, F, Q


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """
    order_in_date = OrderItem.objects.filter(order__date_formation__range=(begin, end))

    join_table = order_in_date.filter(
        order__date_formation__range=(
            F('product__productcost__begin'),
            F('product__productcost__end'),
        )
    )

    max_cost = join_table.values_list(
        'order__number'
    ).annotate(
        cost=Sum(F('count') * F('product__productcost__value'))
    ).order_by(
        '-cost',
        '-order__number'
    ).first()

    return max_cost
