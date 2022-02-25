class MathClock:
    def __init__(self):
        self.__minute = 0
        self.__hour = 0

    def __add__(self, other):
        self.__minute += other
        self.__set_standard_time()

    def __sub__(self, other):
        self.__minute -= other
        self.__set_standard_time()

    def __mul__(self, other):
        self.__hour += other
        self.__set_standard_time()

    def __truediv__(self, other):
        self.__hour -= other
        self.__set_standard_time()

    def __set_standard_time(self):
        self.__hour = (self.__hour + self.__minute // 60) % 24
        self.__minute = self.__minute % 60

        if self.__minute < 0:
            self.__minute += 60

        if self.__hour < 0:
            self.__hour += 24

    def get_time(self):
        return '{:02d}:{:02d}'.format(self.__hour, self.__minute)


