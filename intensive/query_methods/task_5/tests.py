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
    get_average_cost_without_product,
)


class ModelTest(BaseTest):

    def test_january(self):
        self.assertEqual(get_average_cost_without_product('Молоко', date(2021, 1, 1), date(2021, 1, 31)), Decimal(630))

    """
    Нет цены для даты заказа в этом промежутке и без этого товара
    """
    def test_febraury(self):
        self.assertEqual(get_average_cost_without_product('Молоко', date(2021, 2, 1), date(2021, 2, 28)), Decimal(420))

    def test_march(self):
        self.assertEqual(get_average_cost_without_product('Молоко', date(2021, 3, 1), date(2021, 3, 31)), Decimal(0))

    def test_april(self):
        self.assertEqual(get_average_cost_without_product('Молоко', date(2021, 4, 1), date(2021, 4, 30)), Decimal(0))