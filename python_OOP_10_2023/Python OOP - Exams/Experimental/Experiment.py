class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Master_of_Pharmacy(Employee):
    def __init__(self, name, age, salary, is_manager=False):
        super().__init__(name, age, salary)
        self.is_bphu_member = False  # Bulgarian Pharmacy Union member
        self.is_nhif_partner = False  # National Health Insurance Fund (NHIF) partner
        self.is_manager = 

class Bachelor_of_Pharmacy(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)


class app:
    def __init__(self):
        self.pharmacists = []

    @staticmethod
    def check_duplicate_name(name, collection):
        existing_name = next((r for r in collection if r.name == name), None)
        return existing_name

    def add_pharmacist(self, name_, age, salary):
        existing_name = self.check_duplicate_name(name_, self.pharmacists)
        if existing_name:
            return 'Вече има такова име в списъка с фармацевти!'
        new_pharmacist = Pharmacist(name_, age, salary)
        self.pharmacists.append(new_pharmacist)
        return f'{name_} e успешно добавен/a към списъка с фармацевти'


my_app = app()

