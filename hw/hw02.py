class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name

        self.age = age

        self.health = health  # очки здоровья


    def info(self) -> str:
        return f"{self.name}, {self.age} лет, здоровье {self.health}"


    def use_ability(self) -> str:
        """Переопределяется в наследниках"""

        return f"{self.name} использует базовую способность."

class Flyable:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + " летает."

class Swimmable:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + " плавает."

class Invisible:
    def use_ability(self) -> str:
        base = super().use_ability()
        return base + " ставновится невидимым."

class Duck(Flyable, Swimmable, Animal):
    """Утка: умеет летать и плавать"""

class Bat(Flyable, Invisible, Animal):
    """Летучая мышь: умеет летать и становиться невидимой"""

class Frog(Swimmable, Animal):
    """Лягушка: умеет плавать"""

class Phoenix(Flyable, Invisible, Animal):
    """Феникс: умеет летать, становиться неведимым и может возрождаться"""

    def reborn(self) -> str:
        self.health = 200
        return f"{self.name} возрождается из пепла. Здоровье восстановлено до {self.health}."

class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(animal.use_ability())


if __name__ == "__main__":

    zoo = Zoo()

    duck = Duck("Дональд", 3, 80)

    bat = Bat("Бэтти", 5, 60)

    frog = Frog("Кермит", 2, 50)

    phoenix = Phoenix("Феникс", 100, 200)

    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")

    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")

    zoo.perform_show()

    print("\nMRO для Duck:", Duck.__mro__)

    print("MRO для Phoenix:", Phoenix.__mro__)
