from tasks.common import MyException


class ClassFather:
    registered_list = set()

    @classmethod
    def get_name(cls):
        if cls != ClassFather and cls in ClassFather.registered_list:
            return cls()._name

        raise MyException

    @classmethod
    def register(cls):
        if cls == ClassFather:
            raise MyException

        if cls not in ClassFather.registered_list:
            ClassFather.registered_list.add(cls)


class User1(ClassFather):
    _name = 'name1'


class User2(ClassFather):
    _name = 'name2'
