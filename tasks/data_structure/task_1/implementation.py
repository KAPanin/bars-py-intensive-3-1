class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    def __init__(self, *args):
        self.__values = args
        self.__sort_values = tuple(sorted(args))
        self.__len = len(self.__values)

    def __getitem__(self, item):
        return self.__values[item]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        result = 0

        mid = 0
        start = 0
        end = self.__len
        while start <= end:
            mid = (start + end) // 2
            if value == self.__sort_values[mid]:
                result += 1
                break
            if value < self.__sort_values[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if result:
            for i in range(mid + 1, self.__len):
                if value == self.__sort_values[i]:
                    result += 1
                else:
                    break

        return result

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        for i in range(self.__len):
            if value == self.__values[i]:
                return i
        else:
            raise ValueError
