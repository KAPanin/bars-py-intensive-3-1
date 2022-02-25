from tasks.common import MyException


class Value:
    def __init__(self, number):
        if isinstance(number, (int, float)):
            self.number = number
        else:
            try:
                self.number = float(number)
            except ValueError:
                raise MyException

    def __add__(self, other):
        return self.number + other

    def __radd__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __rsub__(self, other):
        return other - self.number

    def __mul__(self, other):
        return self.number * other

    def __rmul__(self, other):
        return self.number * other

    def __truediv__(self, other):
        if other:
            return self.number / other
        else:
            raise MyException

    def __rtruediv__(self, other):
        if self.number:
            return other / self.number
        else:
            raise MyException
