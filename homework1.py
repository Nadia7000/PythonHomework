class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        return 'My cool Car'

    def speed(self):
        return 'Good year!'

    def set_model(self, new_model):
        self.model = new_model

    def new_model(self):
        return f'My new Car is {self.model}'


car = Car('Toyota', '2023')
print(car.model)
print(car.year)

car.set_model('Mercedes')
print(car.new_model())


class My_Car(Car):

    def __init__(self, model, year, color):
        super().__init__(model, year)
        self.color = color

    def test(self):
        return 'I love My new car!'


car_1 = My_Car('Toyota', 2023, 'red')
print(car_1.model)
print(car_1.year)
print(car_1.color)
