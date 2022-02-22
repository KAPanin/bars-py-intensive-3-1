from tasks.common import MyException


class ClassFather:
    registered_list = []

    def get_name(self):
        if hasattr(self, '_name') and self._name in self.registered_list:
            return self._name
        else:
            raise MyException

    def register(self):
        if hasattr(self, '_name') and self._name not in self.registered_list:
            ClassFather.registered_list.append(self._name)
        else:
            raise MyException


class User1(ClassFather):
    _name = 'name1'


class User2(ClassFather):
    _name = 'name2'
