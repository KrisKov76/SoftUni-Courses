from project.meals.meal import Meal


class Dessert(Meal):
    QUANTITY_DESSERT = 30

    def __init__(self, name: str, price: float, quantity = QUANTITY_DESSERT):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
