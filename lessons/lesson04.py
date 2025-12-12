# Dunder methods
# Магические методы — это специальные методы в Python, которые начинаются и
# заканчиваются двумя нижними подчеркиваниями:
# __init__, __str__, __add__, __eq__, __len__, __enter__, __exit__ и т.д.
# Они позволяют объектам вести себя как встроенные типы (числа, списки, строки).


class Test:

    def __init__(self, name="John Doe"):
        self.name = name

    def __str__(self):
        return self.name


# my_obj = Test()
# my_str = [1,22,3]
#
# print(my_obj)
# print(my_str)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +
    def __add__(v2, v1):
        print(v2.x + v1.x)

    # <
    def __lt__(self, other):
        print(self.x)
        print(other.x)

    # >
    # def __gt__(self, other):

    # ==
    # def __eq__(self, other):


v1 = Vector(22, 22)
v2 = Vector(23, 23)


# v3 = v2 < v1


class Mylist:

    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1


# my_list = Mylist()
# print(my_list.count)
# my_list()
# my_list()
# print(my_list.count)


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __to_som(self, data):
        print("Переводим на сом")
        return data

    def __add__(self, other):
        if type(self) == type(other):
            pass
        if self.currency != other.currency:
            data = self.__to_som(other)
        return self.amount + other.amount


class VC:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.view_count = 0

    def __call__(self, user, *args, **kwargs):
        self.view_count += 1
