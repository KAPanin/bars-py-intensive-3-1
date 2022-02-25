from tasks.common import MyException


class ClassFather:
    registered_list = set()

    def get_name(self):
        if type(self) != ClassFather and self in ClassFather.registered_list:
            return self._name

        raise MyException

    def register(self):
        if type(self) == ClassFather:
            raise MyException

        if self not in ClassFather.registered_list:
            ClassFather.registered_list.add(self)


class User1(ClassFather):
    _name = 'name1'


class User2(ClassFather):
    _name = 'name2'
