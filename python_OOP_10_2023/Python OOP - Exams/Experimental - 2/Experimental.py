from abc import ABC, abstractmethod

from fuzzywuzzy import fuzz


class Human(ABC):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def details(self):
        pass


class Pharmacist(Human):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.pharmacists = []

    def details(self):
        return f'Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.weight},'


class Pharmacy:
    def __init__(self, pharmacy_name, telephone_number):
        self.name = pharmacy_name
        self.telephone_number = telephone_number
        self.revenue = 0  # Добавете обороти за всяка аптека
        self.pharmacies = []

    def add_revenue(self, amount):
        self.revenue += amount

        if self.revenue > 10000:
            print(f'Вие регистрирахте оборот над 10 000 лв за аптека {self.name}')

    def get_pharmacists_list(self):
        return [pharmacist.name for pharmacist in self.pharmacies]


class PharmApp:
    def __init__(self):
        self.pharmacists_app = []
        self.pharmacies_app = []

    def check_duplicate_name(self, name, collection):
        existing_name = next((r for r in collection if r.name == name), None)
        return existing_name

    def add_pharmacist(self, name_, age, height, weight):
        existing_name = self.check_duplicate_name(name_, self.pharmacists_app)
        if existing_name:
            return 'Вече има такова име в списъка с фармацевти!'
        new_pharmacist = Pharmacist(name_, age, height, weight)
        self.pharmacists_app.append(new_pharmacist)
        return f'{name_} e успешно добавен/a към списъка с фармацевти'

    def add_pharmacy(self, name, telephone_number):
        pharmacy = self.check_duplicate_name(name, self.pharmacies_app)

        if pharmacy:
            return 'Вече има аптека с това име в списъка с аптеки!'
        new_pharmacy = Pharmacy(name, telephone_number)
        self.pharmacies_app.append(new_pharmacy)
        return f'Аптека {name} e успешно добавенa към списъка с аптеки'

    def assign_pharmacist_to_pharmacy(self, pharmacist_name, pharmacy_name):
        pharmacist = self.check_duplicate_name(pharmacist_name, self.pharmacists_app)
        pharmacy = self.check_duplicate_name(pharmacy_name, self.pharmacies_app)

        if not pharmacist or not pharmacy:
            return 'Фармацевт или аптека с това име не съществува'

        pharmacist.pharmacy = pharmacy
        pharmacy.pharmacies.append(pharmacist)
        return f'{pharmacist.name} e успешно добавен/a към аптека {pharmacy.name}'

    def add_revenue_to_pharmacy(self, pharmacy_name, amount):
        pharmacy = self.check_duplicate_name(pharmacy_name, self.pharmacies_app)

        if not pharmacy:
            return 'Аптека с това име не съществува'

        pharmacy.add_revenue(amount)
        return f'Оборотът от {amount} лв. е добавен за аптека {pharmacy_name}. Нов оборот: {pharmacy.revenue}'

    def get_pharmacy_for_pharmacist(self, query):
        query = query.lower().strip()

        for p in self.pharmacists_app:
            if query == p.pharmacy.telephone_number or query in p.name.lower():

                if p.pharmacy:
                    return f'{p.name} е свързан/а с аптека {p.pharmacy.name}'
                else:
                    return f'{p.name} не е свързан/а с аптека в момента'
            else:
                name_parts = query.split()
                name_similarity = max(fuzz.partial_ratio(query, part) for part in p.name.lower().split())
                if name_similarity >= 70:
                    return f'{p.name} е свързан/а с аптека {p.pharmacy.name}'

        return f'Не е намерено съвпадение за критерия {query}'

    def print_pharmacists_for_pharmacy(self, pharmacy_name):
        pharmacy = self.check_duplicate_name(pharmacy_name, self.pharmacists_app)

        if not pharmacy:
            return 'Аптека с това име не съществува'

        pharmacists_list = pharmacy.get_pharmacists_list()

        if pharmacists_list:
            return f'Фармацевтите към аптека {pharmacy_name} са:\n - {"\n - ".join(pharmacists_list)}'
        else:
            return f'Няма свързани фармацевти към аптека {pharmacy_name}'


myPharm = PharmApp()

print(myPharm.add_pharmacist('Kristian', 47, 165, 100))
print(myPharm.add_pharmacist('Kristian', 47, 165, 100))

print(myPharm.add_pharmacist('Natalia', 46, 165, 70))
print(myPharm.add_pharmacist('Krasimir Kulinski', 36, 175, 65))
print(myPharm.add_pharmacist('Vasilka Jilova', 30, 170, 80,))

print(myPharm.add_pharmacy('Sopharmacy Novotel', '0882368183'))
print(myPharm.add_pharmacy('Sopharmacy Novotel', '0882368183'))
print(myPharm.add_pharmacy('Mareshki 33', '0876878037'))
print(myPharm.add_pharmacy('Sopharmacy Pazardzhik', '0800000001'))

print(myPharm.assign_pharmacist_to_pharmacy('Kristian', 'Sopharmacy Novotel'))
print(myPharm.assign_pharmacist_to_pharmacy('Natalia', 'Sopharmacy Novotel'))
print(myPharm.assign_pharmacist_to_pharmacy('Krasimir Kulinski', 'Sopharmacy Pazardzhik'))
print(myPharm.assign_pharmacist_to_pharmacy('Vasilka Jilova', 'Sopharmacy Novotel'))
print(myPharm.get_pharmacy_for_pharmacist('Kristian'))

print(myPharm.assign_pharmacist_to_pharmacy('Natalia', 'Mareshki 33'))
print(myPharm.get_pharmacy_for_pharmacist('Kul'))
print(myPharm.print_pharmacists_for_pharmacy('Sopharmacy Novotel'))
print(myPharm.add_revenue_to_pharmacy('Sopharmacy Novotel', 5000))
print(myPharm.add_revenue_to_pharmacy('Sopharmacy Novotel', 100000))

