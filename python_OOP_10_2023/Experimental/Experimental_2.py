from abc import ABC, abstractmethod

from fuzzywuzzy import fuzz


class Pharmacist:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pharmacists = []
        self.membership_fee = False

    def add_membership_fee(self):
        self.membership_fee = True

    def details(self):
        pass


class Pharmacy:
    def __init__(self, pharmacy_name, telephone_number):
        self.name = pharmacy_name
        self.telephone_number = telephone_number
        self.revenue = 0  # Добавете обороти за всяка аптека
        self.pharmacy_members = []
        self.is_nhif = False

    def add_revenue(self, amount):
        self.revenue += amount

        if self.revenue > 10000:
            print(f'Вие регистрирахте оборот над 10 000 лв за аптека {self.name}')

    def add_nhif(self):
        self.is_nhif = True


class PharmApp:
    def __init__(self):
        self.pharmacists_app = []
        self.pharmacies_app = []

    def check_duplicate_name(self, name, collection):
        existing_name = next((r for r in collection if r.name == name), None)
        return existing_name

    def add_pharmacist(self, name_, age):
        existing_name = self.check_duplicate_name(name_, self.pharmacists_app)
        if existing_name:
            return 'Вече има такова име в списъка с фармацевти!'
        new_pharmacist = Pharmacist(name_, age)
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
        pharmacy.pharmacy_members.append(pharmacist)
        return f'{pharmacist.name} e успешно добавен/a към аптека {pharmacy.name}'

    def add_revenue_to_pharmacy(self, pharmacy_name, amount):
        pharmacy = self.check_duplicate_name(pharmacy_name, self.pharmacies_app)

        if not pharmacy:
            return 'Аптека с това име не съществува'

        pharmacy.add_revenue(amount)
        return f'Оборотът от {amount} лв. е добавен за аптека {pharmacy_name}. Нов оборот: {pharmacy.revenue}'

    def add_nhif_to_pharmacy(self, pharmacy_name, pharmacist_name):
        pharmacy = self.check_duplicate_name(pharmacy_name, self.pharmacies_app)
        pharmacist = self.check_duplicate_name(pharmacist_name, self.pharmacists_app)

        if not pharmacy:
            return 'Аптека с това име не съществува'

        if not pharmacist.membership_fee:
            return f'{pharmacist.name} не си е заплатил/a чл.внос и не може да работи с РЗОК'

        if pharmacy.is_nhif:
            return f'Aптека {pharmacy_name} вече работи със Здравната каса!'
        pharmacy.add_nhif()
        return f'Aптека {pharmacy_name} с управител {pharmacist.name} е добавена за работа със Здравната каса'

    def get_membership_in_bphu(self, pharmacist_name):
        pharmacist = self.check_duplicate_name(pharmacist_name, self.pharmacists_app)

        if not pharmacist:
            return 'Фармацевт с това име не съществува'

        if pharmacist.membership_fee:
            return f'{pharmacist.name} вече е заплатил/a своя членски внос към БФС'
        pharmacist.add_membership_fee()
        return f'{pharmacist.name} успешно заплати своя членски внос към БФС'

    def get_pharmacy_for_pharmacist(self, query):
        query = query.lower().strip()

        for p in self.pharmacists_app:
            if query == p.pharmacy.telephone_number or query in p.name.lower():

                if p.pharmacy:
                    return f'{p.name} е свързан/а с аптека {p.pharmacy.name}'
                else:
                    return f'{p.name} не е свързан/а с аптека в момента'
            else:
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

    def get_pharmacists_details(self, pharmacist_name):
        pharmacist = self.check_duplicate_name(pharmacist_name, self.pharmacists_app)
        return pharmacist.details()


myPharm = PharmApp()

print(myPharm.add_pharmacist('Kristian', 47))
print(myPharm.add_pharmacist('Kristian', 47))

print(myPharm.add_pharmacist('Natalia', 46))
print(myPharm.add_pharmacist('Krasimir Kulinski', 36))
print(myPharm.add_pharmacist('Vasilka Jilova', 30))

print(myPharm.add_pharmacy('Sopharmacy Novotel', '0882368183'))
print(myPharm.add_pharmacy('Sopharmacy Novotel', '0882368183'))
print(myPharm.add_pharmacy('Marrakesh 33', '0876878037'))
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

print(myPharm.get_pharmacists_details('Kristian'))
print(myPharm.get_membership_in_bphu('Kristian'))
print(myPharm.get_membership_in_bphu('Vasilka Jilova'))

print(myPharm.add_nhif_to_pharmacy('Sopharmacy Novotel', 'Kristian'))
print(myPharm.add_nhif_to_pharmacy('Sopharmacy Novotel', 'Vasilka Jilova'))
