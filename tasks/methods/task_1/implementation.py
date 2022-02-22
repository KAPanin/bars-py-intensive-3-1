class Coffee:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def init_cappuccino(cls):
        coffee = cls(coffee=1/3, hot_milk=1/3, whipped_milk_foam=1/3)
        return coffee

    @classmethod
    def init_latte(cls):
        coffee = cls(coffee=1/4, hot_milk=1/3, whipped_milk_foam=1/3)
        return coffee

    @classmethod
    def init_glace(cls):
        coffee = cls(coffe=1/2, icescream=1/4, grated_chocolate=1.4)
        return coffee
