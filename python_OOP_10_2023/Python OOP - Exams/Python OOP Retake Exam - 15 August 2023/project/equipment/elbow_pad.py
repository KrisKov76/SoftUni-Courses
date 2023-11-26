from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        protection = 90
        price = 25.0
        super().__init__(protection, price)

    def increase_price(self):
        # Увеличаване на цената с 10%
        self.price *= 1.1
