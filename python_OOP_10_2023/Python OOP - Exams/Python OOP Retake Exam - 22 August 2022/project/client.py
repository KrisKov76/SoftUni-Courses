import re


class Client:
    bill = None
    shopping_cart = None

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0


    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        pattern = r'^0\d{9}$'
        if re.match(pattern, value):
            self._phone_number = value
        else:
            raise ValueError("Invalid phone number!")
