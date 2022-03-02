from datetime import (
    date,
)
from decimal import (
    Decimal,
)

from ..tests import (
    BaseTest,
)

from .implementation import (
    get_top_order_by_sum_in_period,
)


class ModelTest(BaseTest):

    def test_january(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 1, 1), date(2021, 1, 31)), ('4', Decimal(630)))

    #  Нет даты 6 заказа в проиежутке даты наличия цены
    def test_febraury(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 2, 1), date(2021, 2, 28)), ('6', Decimal(420)))

    # не верно
    def test_march(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 3, 1), date(2021, 3, 31)), ('7', Decimal(56)))

    def test_april(self):
        self.assertEqual(get_top_order_by_sum_in_period(date(2021, 4, 1), date(2021, 4, 30)), None)