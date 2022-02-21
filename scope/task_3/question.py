"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)


"""
3
3

Внутри функции явно указано, что number это переменная из нелокального пространства имен. Т.е. изменяется именно эта 
переменная. При выводе внутри print_msg number уже изменена.
"""
