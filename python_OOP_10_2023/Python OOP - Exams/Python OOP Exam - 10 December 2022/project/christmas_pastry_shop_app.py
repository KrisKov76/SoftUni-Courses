from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        existing_delicacy = next((r for r in self.delicacies if r.name == name), None)

        if existing_delicacy:
            raise Exception(f"{name} already exists!")
        self.delicacies.append(self.DELICACY_TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        existing_booth_number = next((r for r in self.booths if r.booth_number == booth_number), None)

        if existing_booth_number:
            raise Exception(F'Booth number {booth_number} already exists!')
        self.booths.append(self.BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = next((r for r in self.booths if r.booth_number == booth_number), None)
        if not booth:
            raise Exception(f"No available booth for {booth_number} people!")

        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        if booth:
            self.income += bill  # добавяне на сметката към общия приход на пекарнята
            booth.is_reserved = False
            booth.price_for_reservation = 0
            booth.delicacy_orders = []
            return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        formatted_income = f"{self.income:.2f}"
        return f"Income: {formatted_income}lv."
