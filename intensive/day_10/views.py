from django.http import JsonResponse

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

        if 'delimiter' in request.GET:
            delimiter = request.GET['delimiter']
        else:
            delimiter = ','

        list_operations = request.GET['maths'].split(delimiter)

        for operation in list_operations:
            result_dict[operation] = eval(operation)

    return JsonResponse(result_dict)
