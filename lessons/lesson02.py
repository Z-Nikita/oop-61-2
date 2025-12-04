# Родительский/Супер класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} {self.lvl}"

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"{self.name} Салам!"

    def cast_spell(self):
        return f"{self.name} кастует огненный шар!!!"

class WarriorHero(Hero):
    def attack(self):
        return f"{self.name} наносит удар мечом!!!"

gandalf = MageHero("Gandalf", 100, 1000, 100)
aragon = WarriorHero("Aragon", 100, 1000, 99)

# print(kirito.action())
# print(gandalf.action())
# print(aragon.action())

# print(type(gandalf))
# print(type(kirito))

