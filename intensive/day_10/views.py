from django.http import (
    JsonResponse,
    HttpResponse,
)

from django.db.models import (
    Count,
    Min,
)

from datetime import (
    date,
)
from decimal import (
    Decimal,
)

from .models import (
    Customer,
    Order,
    OrderItem,
    Product,
    ProductCost,
    ProductCount,
)


def calc(request):
    """
    Представление которому в параметре запроса maths через разделитель перечисляются простейшие арифметические операции
    например maths=3*3,10-2,10/5
    по умолчанию в качестве символа разделителя выступает сивол запятой.
    В необязательном параметре delimiter указывается символ разделителя арифметических операций
    например calc/?maths=3*3;10-2;10/5&delimiter=;

    Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
    """
    result_dict = {}

    if request.method == 'GET':

        delimiter = request.GET.get('delimiter', ',')

        list_operations = request.GET['maths'].split(delimiter)

        for operation in list_operations:
            result_dict[operation] = eval(operation)

    return JsonResponse(result_dict)


def query_db(request):
    top_customer = tuple()
    order_count = tuple()

    if request.method == 'GET':

        def str2int(list_str):
            return list(map(lambda i: int(i), list_str))

        begin = str2int(request.GET.get('begin').split('.'))
        end = str2int(request.GET.get('end').split('.'))
        name = request.GET.get('name')

        top_customer = get_top_customer_in_period(
            date(*begin),
            date(*end),
        )
        order_count = get_order_count_by_customer(name)

    return JsonResponse(
        {
            'top_customer': top_customer,
            'order_count': order_count,
        }
    )


def save_db(request):
    milk = Product.objects.create(name='Молоко')

    ProductCount.objects.bulk_create([
        ProductCount(
            product=milk,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=10,
        ),
        ProductCount(
            product=milk,
            begin=date(2021, 2, 1),
            end=date(2021, 2, 28),
            value=4,
        ),
        ProductCount(
            product=milk,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 31),
            value=7,
        )
    ])

    ProductCost.objects.bulk_create([
        ProductCost(
            product=milk,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=Decimal(50),
        ),
        ProductCost(
            product=milk,
            begin=date(2021, 2, 1),
            end=date(2021, 2, 14),
            value=Decimal(60),
        ),
        ProductCost(
            product=milk,
            begin=date(2021, 2, 15),
            end=date(2021, 2, 28),
            value=Decimal(65),
        ),
        ProductCost(
            product=milk,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 31),
            value=Decimal(60),
        )
    ])

    bread = Product.objects.create(name='Хлеб')

    ProductCount.objects.bulk_create([
        ProductCount(
            product=bread,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=100,
        ),
        ProductCount(
            product=bread,
            begin=date(2021, 2, 1),
            end=date(2021, 2, 28),
            value=50,
        ),
        ProductCount(
            product=bread,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 1),
            value=0,
        )
    ])

    ProductCost.objects.bulk_create([
        ProductCost(
            product=bread,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=Decimal(30),
        ),
        ProductCost(
            product=bread,
            begin=date(2021, 2, 1),
            end=date(2021, 2, 14),
            value=Decimal(32),
        ),
        ProductCost(
            product=bread,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 31),
            value=Decimal(35),
        )
    ])

    tea = Product.objects.create(name='Чай')

    ProductCount.objects.bulk_create([
        ProductCount(
            product=tea,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=64,
        ),
        ProductCount(
            product=tea,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 1),
            value=32,
        )
    ])

    ProductCost.objects.bulk_create([
        ProductCost(
            product=tea,
            begin=date(2021, 1, 1),
            end=date(2021, 1, 31),
            value=Decimal(150),
        ),
        ProductCost(
            product=tea,
            begin=date(2021, 2, 1),
            end=date(2021, 2, 14),
            value=Decimal(140),
        ),
        ProductCost(
            product=tea,
            begin=date(2021, 3, 1),
            end=date(2021, 3, 31),
            value=Decimal(160),
        )
    ])

    ivan = Customer.objects.create(name='Иван')
    pavel = Customer.objects.create(name='Павел')
    oleg = Customer.objects.create(name='Олег')

    order_1 = Order.objects.create(
        number='1',
        date_formation=date(2021, 1, 1),
        customer=ivan,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_1,
            product=milk,
            count=1,
        ),
        OrderItem(
            order=order_1,
            product=bread,
            count=1,
        ),
        OrderItem(
            order=order_1,
            product=tea,
            count=1,
        )
    ])

    order_2 = Order.objects.create(
        number='2',
        date_formation=date(2021, 1, 10),
        customer=oleg,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_2,
            product=milk,
            count=3,
        ),
        OrderItem(
            order=order_2,
            product=tea,
            count=2,
        )
    ])

    order_3 = Order.objects.create(
        number='3',
        date_formation=date(2021, 1, 15),
        customer=pavel,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_3,
            product=milk,
            count=6,
        ),
        OrderItem(
            order=order_3,
            product=tea,
            count=1,
        )
    ])

    order_4 = Order.objects.create(
        number='4',
        date_formation=date(2021, 1, 15),
        customer=ivan,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_4,
            product=bread,
            count=1,
        ),
        OrderItem(
            order=order_4,
            product=tea,
            count=4,
        )
    ])

    order_5 = Order.objects.create(
        number='5',
        date_formation=date(2021, 2, 7),
        customer=oleg,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_5,
            product=milk,
            count=4,
        ),
        OrderItem(
            order=order_5,
            product=bread,
            count=2,
        )
    ])

    order_6 = Order.objects.create(
        number='6',
        date_formation=date(2021, 2, 19),
        customer=ivan,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_6,
            product=tea,
            count=3,
        ),
    ])

    order_7 = Order.objects.create(
        number='7',
        date_formation=date(2021, 3, 1),
        customer=pavel,
    )
    OrderItem.objects.bulk_create([
        OrderItem(
            order=order_7,
            product=milk,
            count=8,
        ),
    ])

    return HttpResponse('База данных заполнена')


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


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя
    Args:
        name: имя покупателя
    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    return Order.objects.filter(customer__name=name).count()

