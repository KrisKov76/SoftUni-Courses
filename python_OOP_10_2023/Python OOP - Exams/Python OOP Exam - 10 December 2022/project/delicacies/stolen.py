from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    GINGER_PORTION = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.GINGER_PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 250g - {self.price:.2f}lv."
