class Multiplier:
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        if isinstance(other, Multiplier):
            new_value = self._value + other._value
        else:
            new_value = self._value

        return Multiplier(new_value)

    def __sub__(self, other):
        if isinstance(other, Multiplier):
            new_value = self._value - other._value
        else:
            new_value = self._value

        return Multiplier(new_value)

    def __truediv__(self, other):
        if isinstance(other, Multiplier):
            new_value = self._value / other._value
        else:
            new_value = self._value

        return Multiplier(new_value)

    def __mul__(self, other):
        if isinstance(other, Multiplier):
            new_value = self._value * other._value
        else:
            new_value = self._value

        return Multiplier(new_value)

    def get_value(self) -> int:
        return int(self._value)


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



