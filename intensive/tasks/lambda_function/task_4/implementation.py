class Product:
    def __init__(self, value):
        self.value = value


a = Product(12)
b = Product(7)
c = Product(10)
my_list_product = [a, b, c]

res_list_product = list(filter(lambda prod: prod.value > 10, my_list_product))
