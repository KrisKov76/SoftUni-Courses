from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        protection = 120
        price = 15.0
        super().__init__(protection, price)

    def increase_price(self):
        # Увеличаване на цената с 20%
        self.price *= 1.2
