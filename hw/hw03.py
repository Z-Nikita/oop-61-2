# 1) Encapsulation

# class Product:
#     def __init__(self, name, price, discount = 0):
#         self.name = name
#         self._price = price
#         self.__discount = 0
#         self.__vip_applied = False
#         self.set_discount(discount)
#
#     __VIP_CODE = "VIP123"
#
#     def set_discount(self, percent):
#         if 0 <= percent <= 50:
#             self.__discount = percent
#         else:
#             print("Ошибка: скидка должна быть от 0 до 50 процентов")
#
#     def get_price(self):
#         total_discount = self.__discount
#         if self.__vip_applied:
#             total_discount += 5
#
#         final_price = self._price * (100 - total_discount) / 100
#         return final_price
#
#     def apply_extra_discount(self, secret_code):
#         if secret_code == self.__VIP_CODE:
#             if not self.__vip_applied:
#                 self.__vip_applied = True
#         else:
#             print("Неверный код")
#
# p = Product("Iphone", 1000)
#
# p.set_discount(20)
# print("Цена со скидкой:", p.get_price())
#
# p.apply_extra_discount("VIP123")
# print("Цена после VIP:", p.get_price())
#
# p.apply_extra_discount("wrong")
# print("Цена итоговая:", p.get_price())

# 2) Abstract

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")

class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        data = {"type": "crypto", "amount": amount, "currency": "USDT"}
        print(data)

    def refund(self, amount):
        data = {"type": "crypto_refund", "amount": amount, "currency": "USDT"}
        print(data)

class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)


processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)