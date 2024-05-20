import re


class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Pharmacist_profile(Employee):
    def __init__(self, name, email, prof_mail):
        super().__init__(name, email)
        self.prof_mail = prof_mail

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not self._is_valid_email(value):
            raise ValueError("Invalid email address")
        self._email = value

    @staticmethod
    def _is_valid_email(email):
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(email_pattern, email))

    def __str__(self):
        return f'{self.name}, {self.email}, {self.prof_mail}'


class Pharmacy:
    def __init__(self, pharmacy_name):
        self.name = pharmacy_name
        self.members = []

    def get_member_count(self):
        return len(self.members)

    def get_pharmacists_info(self):
        return [f'- {str(member)}' for member in self.members]

class App:
    def __init__(self):
        self.pharmacists = []
        self.pharmacies = []

    @staticmethod
    def check_existing_name(name_, collection):
        existing_name = next((r for r in collection if r.name == name_), None)
        return existing_name

    def add_pharmacist(self, name, email_, prof_mail_):
        pharmacist = next((r for r in self.pharmacists
                           if r.name == name
                           or r.email == email_
                           or r.prof_mail == prof_mail_), None)

        gender_suffix = 'а' if name.endswith('a') else ''

        if pharmacist:
            return 'Вече има фармацевт с такова име'
        new_pharmacist = Pharmacist_profile(name, email_, prof_mail_)
        self.pharmacists.append(new_pharmacist)
        return f'Фармацевтът {name} беше добавен{gender_suffix}'

    def add_pharmacy(self, name):
        pharmacy = self.check_existing_name(name, self.pharmacies)

        if pharmacy:
            return 'Вече има aптека с такова име'
        new_pharmacy = Pharmacy(name)
        self.pharmacies.append(new_pharmacy)
        return f'Аптеката {name} e добавенa към списъка с аптеки'

    def add_pharmacist_to_pharmacy(self, pharmacist_name, pharmacy_name):
        pharmacist = self.check_existing_name(pharmacist_name, self.pharmacists)
        pharmacy = self.check_existing_name(pharmacy_name, self.pharmacies)

        gender_suffix = 'а' if pharmacist_name.endswith('a') else ''

        if pharmacy and pharmacist:
            if pharmacist in pharmacy.members:
                return f'Фармацевт {pharmacist.name} вече е добавен{gender_suffix} към аптека {pharmacy_name}'
            pharmacy.members.append(pharmacist)
            return f'Фармацевт {pharmacist.name} е добавен{gender_suffix} към аптека {pharmacy_name}'
        else:
            return 'Грешка при добавянето на фармацевт към аптека. Моля, проверете въведените данни.'


my_app = App()
print(my_app.add_pharmacist('Kristian', 'kova4ev2012@gmail.com', 'kristian.kovachev@sopharmacy.bg'))
print(my_app.add_pharmacist('Lenka', 'lenka@gmail.com', 'lenka.kosanova@sopharmacy.bg'))
print()
print(my_app.add_pharmacy('Sopharmacy Novotel'))
print()
print(my_app.add_pharmacist_to_pharmacy('Kristian', 'Sopharmacy Novotel'))
print(my_app.add_pharmacist_to_pharmacy('Lenka', 'Sopharmacy Novotel'))
print()
pharmacy_info = my_app.check_existing_name('Sopharmacy Novotel', my_app.pharmacies)
if pharmacy_info:
    member_count = pharmacy_info.get_member_count()
    print(f'Брой на членовете на аптеката {pharmacy_info.name}: {member_count}')

    for info in pharmacy_info.get_pharmacists_info():
        print(info)
else:
    print('Аптека с това име не беше намерена.')
