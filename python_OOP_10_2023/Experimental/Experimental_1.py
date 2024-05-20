class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Pharmacist(Employee):
    def __init__(self, name, age, qualification, salary, is_manager=False):
        super().__init__(name, age, salary)
        self.qualification = qualification
        self.is_manager = is_manager
        self.is_bphu_member = False

    def __str__(self):
        return f"{self.name}({self.age})"


class Pharmacy:
    def __init__(self, pharmacy_name, number_of_employees):
        self.name = pharmacy_name
        self.number_of_employees = number_of_employees
        self.is_nhif_partner = False
        self.members = []  # пази списък с всички фармацевти към съответната аптека.
        self.p_medicines = []
        self.manager_name = None

    def set_manager_name(self, manager_name):
        self.manager_name = manager_name

    def get_info(self):
        pharmacist_names = [pharmacist.name for pharmacist in self.members]
        info = (f"{self.name} - "
                f"Брой служители: {len(self.members)} от {self.number_of_employees}\n"
                f"Членове на БФС: {', '.join(pharmacist_names)}\n"
                f"Управител: {self.manager_name}\n"
                f"Аптеката работи със Здравна каса - ДА/НЕ: {'ДА' if self.is_nhif_partner else 'НЕ'}")
        return info


class Medicine:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class App:
    def __init__(self):
        self.pharmacists = []
        self.pharmacies = []
        self.medicines = []

    @staticmethod
    def check_existing_name(name, collection):
        existing_name = next((r for r in collection if r.name == name), None)
        return existing_name

    def add_pharmacist(self, name_, age, qualification, salary, is_manager):
        pharmacist = self.check_existing_name(name_, self.pharmacists)

        if pharmacist:
            return 'Вече има такова име в списъка с фармацевти!'

        new_pharmacist = Pharmacist(name_, age, qualification, salary, is_manager)
        self.pharmacists.append(new_pharmacist)
        return f'{name_} e успешно добавен/a към списъка с фармацевти'

    def add_pharmacy(self, pharmacy_name_, number_of_employees_):
        pharmacy = self.check_existing_name(pharmacy_name_, self.pharmacies)

        if pharmacy:
            return 'Вече има такава аптека в списъка!'

        new_pharmacy = Pharmacy(pharmacy_name_, number_of_employees_)
        self.pharmacies.append(new_pharmacy)
        return f'{pharmacy_name_} e успешно добавенa към списъка с аптеки'

    def add_medicine_to_pharmacy(self, medicine_name, pharmacy_name):
        medicine = self.check_existing_name(medicine_name, self.medicines)
        pharmacy = self.check_existing_name(pharmacy_name, self.pharmacies)

        if medicine in pharmacy.p_medicines:
            return f'{medicine_name} вече е добавен към номенклатурата на аптека {pharmacy_name}!'
        pharmacy.p_medicines.append(medicine)
        return f'{medicine_name} успешно добавен към номенклатурата на аптека {pharmacy_name}!'

    def add_pharmacist_to_bphu(self, pharmacist_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)

        if not pharmacist:
            return f'Фармацевт {pharmacist_name} не съществува и не може да бъде член на БФС'

        if pharmacist.is_bphu_member:
            return f'{pharmacist.name} вече членува в БФС'
        pharmacist.is_bphu_member = True
        return f'{pharmacist.name} успешно заплати своя чл.внос и вече е член на БФС'

    def add_pharmacist_to_pharmacy(self, pharmacist_name, pharmacy_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)
        pharmacy = self.check_existing_name(pharmacy_name, self.pharmacies)

        if not pharmacist:
            return f'Фармацевт {pharmacist_name} не съществува!'

        if not pharmacy:
            return f'Аптека {pharmacy_name} не съществува!'

        if not pharmacist.is_bphu_member:
            return f'{pharmacist_name} не е член на БФС!'

        if pharmacist in pharmacy.members:
            return f'{pharmacist.name} вече е добавен/а към аптеката {pharmacy.name}!'
        pharmacy.members.append(pharmacist)
        return f'{pharmacist.name} успешно добавен/а към аптеката {pharmacy.name}!'

    def manager_status(self, pharmacist_name, pharmacy_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)
        pharmacy = self.check_existing_name(pharmacy_name, self.pharmacies)

        if pharmacist and not pharmacy.manager_name:
            pharmacist.is_manager = True
            pharmacy.set_manager_name(pharmacist_name)
            return f"Статусът на {pharmacist_name} беше променен на мениджър."
        return f'Аптеката вече има управител и неговото име е {pharmacy.manager_name}'

    def add_pharmacy_to_nhif_partners(self, pharmacy_name, pharmacist_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)
        pharmacy = self.check_existing_name(pharmacy_name, self.pharmacies)

        if not pharmacist:
            return f'Фармацевт {pharmacist_name} не съществува!'

        if not pharmacy:
            return f'Аптека {pharmacy_name} не съществува!'

        if pharmacist not in pharmacy.members:
            return f'{pharmacist_name} не работи в тази аптека и не може да сключи договор с НЗОК'

        if not pharmacist.is_bphu_member:
            return f'{pharmacist_name} не е член на БФС!'

        if pharmacist.qualification != 'Master_of_Pharmacy':
            return f'{pharmacist_name} не е магистър-фармацевт и не може да сключва договор с НЗОК'

        if not pharmacist.is_manager:
            return f'{pharmacist_name} не e управител и не може да сключи договор с НЗОК'

        if pharmacy.is_nhif_partner:
            return f'Аптека {pharmacy.name} вече има договор с НЗОК'

        pharmacy.is_nhif_partner = True
        return f'{pharmacy_name} е добавена към договорните партньори на НЗОК, с управител {pharmacist_name}'

    def get_pharmacist_info(self, pharmacist_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)

        if not pharmacist:
            return f'Фармацевт {pharmacist_name} не съществува в списъка с фармацевти!'

        pharmacy_name = next((pharmacy.name for pharmacy in self.pharmacies if pharmacist in pharmacy.members), None)

        info = (f'Име: {pharmacist.name}\n'
                f'Възраст: {pharmacist.age}\n'
                f'Квалификация: {pharmacist.qualification}\n'
                f'Заплата: {pharmacist.salary}\n'
                f'Управител: {"ДА" if pharmacist.is_manager else "НЕ"}\n'
                f'Аптека: {pharmacy_name}\n'
                f'Член на БФС: {"ДА" if pharmacist.is_bphu_member else "НЕ"}')

        return info

    def get_pharmacist_names(self):
        return [pharmacist.name for pharmacist in self.pharmacists]

    def get_pharmacy_names(self):
        return [pharmacy.name for pharmacy in self.pharmacies]

    def get_pharmacists_in_bphu(self):
        return [pharmacist.name for pharmacist in self.pharmacists]


my_app = App()

print(my_app.add_pharmacist('Kristian', 47, 'Master_of_Pharmacy', 3200, False))
print(my_app.add_pharmacist('Vasilka', 30, 'Master_of_Pharmacy', 2200, False))
print(my_app.add_pharmacist('Vencislava', 26, 'Bachelor_of_Pharmacy', 1200, False))
print(my_app.add_pharmacist('Hristo', 50, 'Master_of_Pharmacy', 2300, False))
print()
print("Имена на фармацевти:", my_app.get_pharmacist_names())
print()
print(my_app.add_pharmacy('Sopharmacy Novotel', 5))
print(my_app.add_pharmacy('Sopharmacy Maritsa', 4))
print()
print("Имена на аптеки:", my_app.get_pharmacy_names())
print()
print(my_app.add_pharmacist_to_bphu('Kristian'))
print(my_app.add_pharmacist_to_bphu('Vasilka'))
print(my_app.add_pharmacist_to_bphu('Vencislava'))
print(my_app.add_pharmacist_to_bphu('Hristo'))
print()
print("Фармацевти, членуващи в БФС:", my_app.get_pharmacists_in_bphu())
print()
print(my_app.add_pharmacist_to_pharmacy('Kristian', 'Sopharmacy Novotel'))
print(my_app.add_pharmacist_to_pharmacy('Vasilka', 'Sopharmacy Novotel'))
print(my_app.add_pharmacist_to_pharmacy('Vencislava', 'Sopharmacy Novotel'))
print(my_app.add_pharmacist_to_pharmacy('Hristo', 'Sopharmacy Maritsa'))
print()
print(my_app.manager_status('Kristian', 'Sopharmacy Novotel'))
print(my_app.manager_status('Vasilka', 'Sopharmacy Novotel'))
print(my_app.add_pharmacy_to_nhif_partners('Sopharmacy Novotel', 'Kristian'))
print()

pharmacy_info = next((pharmacy.get_info() for pharmacy in my_app.pharmacies
                      if pharmacy.name == 'Sopharmacy Novotel'), None)
if pharmacy_info:
    print(pharmacy_info)

print()

pharmacist_info = my_app.get_pharmacist_info('Vencislava')
print(pharmacist_info)
print(my_app)
