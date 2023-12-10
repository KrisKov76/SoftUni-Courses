class Pharmacist(Human):
    def __init__(self, name, age, height, weight, pharmacy):
        super().__init__(name, age, height, weight)
        self.pharmacy = pharmacy
