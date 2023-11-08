from project.food.food import Food


class Dessert(Food):
    PRICE = 5.00001
    def __init__(self, name: str, grams: float, calories: float):
        super().__init__(name, self.PRICE, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories
