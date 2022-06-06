class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def walk(self):
        return print('I know how to walk')

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};'


class SchoolWorker(Person):
    def __init__(self, name, surname, age, gender, number_school):
        super().__init__(name, surname, age, gender)
        self.number_school = number_school

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};'


class Administrator(SchoolWorker):
    def __init__(self, name, surname, age, gender, number_school, job_title):
        super().__init__(name, surname, age, gender, number_school)
        self.job_title = job_title

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};' \
               f'\nJob title - {self.job_title};'


class TechnicalWorker(SchoolWorker):
    def __init__(self, name, surname, age, gender, number_school, work_skills):
        super().__init__(name, surname, age, gender, number_school)
        self.work_skills = work_skills

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};' \
               f'\nWork Skills - {self.work_skills};'


class HeadTeacher(Administrator):
    def __init__(self, name, surname, age, gender, number_school, job_title):
        super().__init__(name, surname, age, gender, number_school, job_title)

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};' \
               f'\nJob title - {self.job_title};'


class Cleaner(TechnicalWorker):
    def __init__(self, name, surname, age, gender, number_school, work_skills, ):
        super().__init__(name, surname, age, gender, number_school, work_skills)

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};' \
               f'\nWork Skills - {self.work_skills};'


class Electrician(TechnicalWorker):
    def __init__(self, name, surname, age, gender, number_school, voltage, ):
        super().__init__(name, surname, age, gender, number_school, voltage)
        self.voltage = voltage

    def __str__(self):
        return f'Name - {self.name};' \
               f'\nSurname - {self.surname};' \
               f'\nAge - {self.age};' \
               f'\nGender - {self.gender};' \
               f'\nNumber - School {self.number_school};' \
               f'\nМах voltage - {self.voltage};'


p = Cleaner('Peter', 'Derevniuk', 26, 'Mile', 3, 'I clean well')
print(p)


