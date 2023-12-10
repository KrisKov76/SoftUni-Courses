from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def details(self):
        pass
