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

    def add_doctor(self):
        self.profession = 'doctor'
        return self.profession

    def add_policeman(self):
        self.profession = 'policeman'
        return self.profession

    def add_teacher(self):
        self.profession = 'teacher'
        return self.profession

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.profession}, {self.age}, {self.country}, {self.get_email()}, {self.birth_year()}'


a = User('Pavel', 'Spinok', 26, 'Kbr', 'men', 'polisman')
print(a.get_email())
print(a.birth_year())
print(a)
a.add_teacher()
print(a)