from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(amount)


class PaypalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(amount)


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.process_payment(amount)


credit_card = CreditCardPayment()
paypal = PaypalPayment()

processor = PaymentProcessor(credit_card)
processor2 = PaymentProcessor(paypal)

processor.process_payment(100)
processor2.process_payment(200)
