class Animal:  # клас, шаблон
    def __init__(self, name):  # метод (methods) с инициализатор (конструктор)
        self.name = name  # модел е характеристика (Data Attributes)

    def sleep(self):
        return "sleeping..."


# aтрибутите на класа са и характеристиките и методите

# инстанция наричаме конкретния обект, който сме създали в този клас - имаме клас телефон и различни инстанции,
# различни телефони

animal = Animal("cat")
print(animal.sleep())