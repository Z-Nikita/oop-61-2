# 1 Task
#
# PERMISSIONS = {
#     "admin": ["start", "ban", "stop"],
#     "user": ["start", "message"]
# }
#
# class User:
#     def __init__(self, username, role):
#         self.username = username
#         self.role = role
#
# def check_access(func):
#     def secured(self, user, text=""):
#         command = func.__name__
#
#         exists = False
#         for role in PERMISSIONS:
#             if command in PERMISSIONS[role]:
#                 exists = True
#
#         if exists:
#             if user.role in PERMISSIONS:
#                 if command in PERMISSIONS[user.role]:
#                     func(self, user, text)
#                 else:
#                     print(f'Пользователь {user.username} не может выполнять команду "{command}"')
#             else:
#                 print(f'Неизвестная роль "{user.role}" у пользователя {user.username}')
#         else:
#             print(f'Команда "{command}" не существует')
#
#     return secured
#
# class CommandHandler:
#     @check_access
#     def start(self, user, text=""):
#         print(f"Пользователь {user.username} ({user.role}) выполняет команду start")
#
#     @check_access
#     def ban(self, user, text=""):
#         print(f"Пользователь {user.username} ({user.role}) выполняет команду ban")
#
#     @check_access
#     def stop(self, user, text=""):
#         print(f"Пользователь {user.username} ({user.role}) выполняет команду stop")
#
#     @check_access
#     def message(self, user, text=""):
#         if text == "":
#             print(f"Пользователь {user.username} отправил сообщение")
#         else:
#             print(f"Пользователь {user.username} отправил сообщение: {text}")
#
# if __name__ == "__main__":
#     user1 = User("Alice", "admin")
#     user2 = User("Bob", "user")
#
#     handler = CommandHandler()
#
#     print("--- Alice ---")
#     handler.start(user1)
#     handler.ban(user1)
#
#     print("\n--- Bob ---")
#     handler.start(user2)
#     handler.ban(user2)
#     handler.message(user2, "Привет!")

# 2 Task

def log_action(func):
    def inner(*args, **kwargs):
        print("Выполняю:", func.__name__)
        return func(*args, **kwargs)
    return inner

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class BankAccount:
    bank_name = "Demo Bank"
    created_count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def is_positive(amount):
        return amount > 0

    @classmethod
    def open_account(cls, owner, initial_balance):
        if cls.is_positive(initial_balance):
            cls.created_count = cls.created_count + 1
            print(f"Счет открыт в банке: {cls.bank_name}. Всего счетов: {cls.created_count}")
            return cls(owner, initial_balance)
        else:
            print("Нельзя открыть счет: начальный баланс должен быть > 0")
            return None

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print("Новое название банка:", cls.bank_name)

    @log_action
    def deposit(self, amount):
        if self.is_positive(amount):
            self.balance = self.balance + amount
            print(f"Пополнение: +{amount}. Баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть > 0")

    @log_action
    def withdraw(self, amount):
        if self.is_positive(amount):
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Снятие: -{amount}. Баланс: {self.balance}")
            else:
                print("Недостаточно средств")
        else:
            print("Сумма снятия должна быть > 0")

    def show_info(self):
        print(f"Счет владельца: {self.owner.username}, баланс: {self.balance}, банк: {self.bank_name}")

if __name__ == "__main__":
    user1 = User("Alice", "admin")
    user2 = User("Bob", "user")

    BankAccount.change_bank_name("KG Demo Bank")

    acc1 = BankAccount.open_account(user1, 500)
    acc2 = BankAccount.open_account(user2, 1000)

    print("\n--- Информация о счетах ---")
    if acc1:
        acc1.show_info()
    if acc2:
        acc2.show_info()

    print("\n--- Операции (instance methods + decorator) ---")
    if acc2:
        acc2.deposit(200)
        acc2.withdraw(150)
        acc2.withdraw(5000)
        acc2.deposit(-10)