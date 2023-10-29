class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


ivan = Person("Ivan", 30)
georgi = Person("Georgi",30)
lili = Person("Lili", 20)

print(ivan.age)
ivan.birthday()
lili.birthday()
print(lili.age)
print(ivan.age)

