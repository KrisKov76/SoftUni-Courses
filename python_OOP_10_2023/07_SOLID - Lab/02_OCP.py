from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Turtle(Animal):
    def make_sound(self):
        return "turtle sound"


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle()]
print(animal_sound(animals))
