import json

from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)

import sys
import time


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_start = time.time()

        response = self.get_response(request)

        duration = time.time() - time_start
        size_of_response = sys.getsizeof(response)
        print(
            f'Время выполнения запроса: {duration}',
            f'Размер ответа в байтах: {size_of_response}',
            sep='\n',
        )

        return response


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if type(response) == JsonResponse:
            result_dict = json.loads(response.content)

            result = ''
            for key, value in result_dict.items():
                result += f'<p>{key} = {str(value)}</p>'

            response = HttpResponse(result)

        return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """
    @staticmethod
    def process_exception(request, exception):
        return HttpResponse(f"Ошибка: {exception}")
