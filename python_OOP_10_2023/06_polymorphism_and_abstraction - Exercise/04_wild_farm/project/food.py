from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod  # щом не е указано кое да е абстрактно, правим инит-а
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)
