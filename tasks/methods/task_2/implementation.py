from tasks.common import MyException


class ClassFather:
    registered_list = []

    def get_name(self):
        if type(self) == ClassFather:
            raise MyException

        if self in self.registered_list:
            return self._name
        else:
            raise MyException

    def register(self):
        if type(self) == ClassFather:
            raise MyException

        if self not in self.registered_list:
            ClassFather.registered_list.append(self)


class User1(ClassFather):
    _name = 'name1'


class User2(ClassFather):
    _name = 'name2'
