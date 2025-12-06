# Инкапсуляция

# public — обычные атрибуты
# _protected — одно подчёркивание: «не трогай, это внутреннее»
# __private — два подчёркивания: работает name-mangling (настоящее скрытие)

import random


class BankAccount:

    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

        def get_balance(self, password):
            if password == self.__password:
                return self._balance
            return 'не верный пароль'

    def get_money(self, password, amount):
        if password == self.__password:
            self._balance -= amount
            return self._balance
        return 'не верный пароль'

    def _random_password(self):
        return random.randint(100000, 999999)

    def reset_password(self, old_password):
        if self.__password == old_password:
            new_pass = self._random_password()
            self.__password = new_pass
            return self.__password
        return 'не верный пароль'

ardager = BankAccount("Ardager", 100, "Def2638")

# print(ardager.reset_password("Def2638"))


# Абстракция

from abc import ABC, abstractmethod


# Абстрактный класс Animal
class Animanl(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def voce(self):
        pass

class Dog(Animanl):

    def move(self):
        return "Ходит"

    def voce(self):
        return "Гав Гав"

my_dog = Dog()

class User:

    def __init__(self, name, country):
        self.name = name
        self.country = country


ardager2 = User("Ardager", "KG")
ardager3 = User("Ardager", "RU")

class ABCSendOTP(ABC):
    @abstractmethod
    def send_otp(self, user):
        pass

class KGSendOTP(ABCSendOTP):
    def send_otp(self, user):
        sms = f"<Text>1234</Text><PhoneNumber>+996779280699</PhoneNumber>"
        print(sms)

class RUSendOTP(ABCSendOTP):
    def send_otp(self, user):
        sms = {
            'text': "1234",
            'phoneNumber': "+7792300903"
        }
        print(sms)

kg = KGSendOTP()
ru = RUSendOTP()

class Register:
    def __init__(self, country1, country2):
        self.countryKG = country1
        self.countryRU = country2

    def register(self, user):

        if user.country == "KG":
            self.countryKG.send_otp()
        elif user.country == "RU":
            self.countryRU.send_otp()

register = Register(kg, ru)

user_name = input("Ввудите имя: ")
user_country = input("Введите страну: ")
my_user = User(user_name, user_country)
register.register(my_user)

# register.register(ardager3)
# register.register(ardager2)