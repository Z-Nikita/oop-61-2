# HeroMage
# hero_mage

class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def base_method(self):
        return f"base action {self.name}"

# объект/экземпляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

print(asuna.base_method())
# объект/экземпляр на основе класса
my_text = "Just text"
my_text_2 = "Just text 2"
my_int = 123
my_list = (1,2,3,45)

# print(type(kirito))
# print(type(my_text))
# print(my_text)