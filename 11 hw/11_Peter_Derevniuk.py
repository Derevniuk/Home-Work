import datetime


class User:

    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    @property
    def get_email(self):
        email = f'{self.name.lower()}.{self.surname.lower()}@gmail.com'
        return email

    @property
    def birth_year(self):
        birth_year = int(datetime.datetime.now().year) - int(self.age)
        return birth_year

    @staticmethod
    def policeman(cls):
        policeman_1 = User('Bob', 'Resot', 20, 'Div', 'men', 'policeman')
        return policeman_1

    @staticmethod
    def doctor(cls):
        doctor_1 = User('Bob', 'Resot', 20, 'Div', 'men', 'policeman')
        return doctor_1

    @staticmethod
    def teacher(cls):
        teacher_1 = User('Bob', 'Resot', 20, 'Div', 'men', 'teacher')
        return teacher_1

    def __str__(self):
        return f'{self.profession}, {self.name}'


a = User('Peter', 'Derevniuk', 28, 'Kbr', 'men', 'doctor')

print(a.teacher(User))
