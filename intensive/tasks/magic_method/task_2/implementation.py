from datetime import datetime, timedelta


class MathClock:
    def __init__(self):
        now = datetime.now()
        self.__time = datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0)

    def __add__(self, other):
        self.__time += timedelta(minutes=int(other))

    def __sub__(self, other):
        self.__time -= timedelta(minutes=int(other))

    def __mul__(self, other):
        self.__time += timedelta(hours=int(other))

    def __truediv__(self, other):
        self.__time -= timedelta(hours=int(other))

    def get_time(self):
        return self.__time.strftime('%H:%M')


