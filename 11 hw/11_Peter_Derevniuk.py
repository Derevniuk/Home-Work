import datetime


class User:

    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def get_email(self):
        return f'{str(self.name).lower()}.{str(self.surname).lower()}@gmail.com'

    def birth_year(self):
        return datetime.datetime.now().year - self.age


a = User('Pavel', 'Spinok', 26, 'Kbr', 'men', 'doctor')
print(a.get_email())
print(a.birth_year())