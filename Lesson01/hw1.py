class Laptop:
    """
    Класс Laptop — описывает ноутбук.
    """

    def __init__(self, brand, model, ram_gb):
        """
        Инициализатор ноутбука.

        :param brand: фирма (бренд) ноутбука
        :param model: модель ноутбука
        :param ram_gb: объем оперативной памяти в гигабайтах
        """
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.battery = 100           # заряд батареи в процентах
        self.is_power_on = False     # включен ли ноутбук

    def power_on(self):
        """Включить ноутбук."""
        if self.is_power_on:
            return f"{self.brand} {self.model} уже включен."
        if self.battery <= 0:
            return f"{self.brand} {self.model} не может включиться - батарея разряжена."
        self.is_power_on = True
        return f"{self.brand} {self.model} включен и готов к работе."

    def power_off(self):
        """Выключить ноутбук."""
        if not self.is_power_on:
            return f"{self.brand} {self.model} уже выключен."
        self.is_power_on = False
        return f"{self.brand} {self.model} выключен."

    def use(self, hours):
        """
        Использовать ноутбук какое-то количество часов.
        Заряд батареи уменьшается.

        :param hours: количество часов использования
        """
        if not self.is_power_on:
            return f"{self.brand} {self.model} выключен. Сначала включите ноутбук."
        if hours <= 0:
            return "Время использования должно быть больше нуля."

        # каждый час использования минус 15% батареи
        battery_usage = hours * 15
        if battery_usage >= self.battery:
            self.battery = 0
            self.is_power_on = False
            return f"Батарея разрядилась во время работы. {self.brand} {self.model} выключился."
        else:
            self.battery -= battery_usage
            return f"Вы поработали {hours} ч. Остаток батареи: {self.battery}%."

    def charge(self):
        """Полностью зарядить ноутбук."""
        self.battery = 100
        return f"{self.brand} {self.model} полностью заряжен на 100%."

    def info(self):
        """Информация о ноутбуке."""
        status = "включен" if self.is_power_on else "выключен"
        return (f"Ноутбук: {self.brand} {self.model}, RAM: {self.ram_gb} GB, "
                f"заряд: {self.battery}%, статус: {status}")

laptop1 = Laptop("Lenovo", "Legion", 24)
laptop2 = Laptop("Apple", "MacBook ", 8)
laptop3 = Laptop("Acer", "Aspire", 16)

# Legion
print(laptop1.info())
print(laptop1.power_on())
print(laptop1.use(3))
print(laptop1.info())
print(laptop1.use(5))
print(laptop1.info())
print(laptop1.charge())
print(laptop1.info())

# MacBook
print("\n" + laptop2.info())
print(laptop2.power_on())
print(laptop2.use(1))
print(laptop2.info())
print(laptop2.charge())
print(laptop2.info())
print(laptop2.power_on())
print(laptop2.use(0))

# Aspire
print("\n" + laptop3.info())
print(laptop3.use(2))
print(laptop3.info())
print(laptop3.power_on())
print(laptop3.info())
print(laptop3.power_off())
print(laptop3.info())
