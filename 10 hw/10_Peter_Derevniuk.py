class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    @staticmethod
    def start_car(self):
        print("Aвтомобиль заведен")

    @staticmethod
    def stop_car(self):
        print("Автомобиль заглушен")

    def year_car(self, year):
        self.year = year

    def year_type(self, type):
        self.type = type

    def year_color(self, color):
        self.color = color

    def __str__(self):
        return f'{self.year}, {self.type}, {self.color}'


audi = Car('Green', 'passenger', 2021)
audi.color = 'Blue'
print(audi)
