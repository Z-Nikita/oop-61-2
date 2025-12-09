from abc import ABC, abstractmethod

# 1
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

# 2
class MageHero(Hero):
    def __int__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __int__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

# 3 - 4
class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password = self.__password

