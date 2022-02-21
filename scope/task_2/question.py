"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


"""
Test message
None

Переменная  message в функции data_transmitter является nonlocal переменной. Т.к внутри этой функции нет локальной 
переменной с именем message, то она берется из пространства имен на уровень выше. В данном случае nonlocal.
Функция transmit_to_space ничего не возвращает, соответственно на печать пойдет None.
"""
