class Multiplier:
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return Multiplier(self._value + self.__check(other))

    def __sub__(self, other):
        return Multiplier(self._value - self.__check(other))

    def __truediv__(self, other):
        return Multiplier(self._value / self.__check(other))

    def __mul__(self, other):
        return Multiplier(self._value * self.__check(other))

    def __radd__(self, other):
        return Multiplier(self._value + self.__check(other))

    def __rsub__(self, other):
        return Multiplier(self.__check(other) - self._value)

    def __rtruediv__(self, other):
        return Multiplier(self.__check(other) / self._value)

    def __rmul__(self, other):
        return Multiplier(self._value * self.__check(other))

    def get_value(self) -> int:
        return int(self._value)

    @staticmethod
    def __check(other):
        """
        Проверяет тип входного аргумента

        Возвращает число
        """
        if isinstance(other, Multiplier):
            return other._value
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        super().__init__(value * 1e2)


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        super().__init__(value * 1e3)


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        super().__init__(value * 1e6)



