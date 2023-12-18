# exercise to practise OOP principal


class Vehicle:
    # parent class Vehicle with model name and mileage properties
    type = 'Vehicle'

    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def display_properties(self):
        # method for print properties of class Vehicle
        print(f'type: {self.type}')
        print(f'model: {self.model}')
        print(f'mileage: {self.mileage}')

    def __str__(self):
        # method for creating a string representation of the Vehicle
        return f'type: {self.type}\nmodel: {self.model}\nmileage: {self.mileage}'


class Bus(Vehicle):
    # child class Bus with additional property capacity
    type = 'bus'

    def __init__(self, model, mileage, capacity):
        super().__init__(model, mileage)
        self.capacity = capacity

    # def display_properties(self):
    #     # method for print properties of parental class and child class Bus
    #     super().display_properties()
    #     print(f'capacity: {self.capacity}')

    def __str__(self):
        # method for creating a string representation of the Bus
        return f'{super().__str__()}\ncapacity: {self.capacity}'


class Car(Vehicle):
    # child class Car with additional property maximal speed
    type = 'car'

    def __init__(self, model, mileage, max_speed):
        super().__init__(model, mileage)
        self.max_speed = max_speed

    # def display_properties(self):
    #     # method for print properties of parental class and child class Car
    #     super().display_properties()
    #     print(f'maximal speed: {self.max_speed}')

    def __str__(self):
        # method for creating a string representation of the Car
        return f'{super().__str__()}\nmaximal speed: {self.max_speed}'


# definition of two instances of child class Bus and Car
Vehicle1 = Car('Octavia', 110000, 180)
Vehicle2 = Bus('Volvo TR', 250000, 80)

print(type(Vehicle1))
print(isinstance(Vehicle1, Vehicle))
print(isinstance(Vehicle1, Car))
# Vehicle1.display_properties()
print(Vehicle1)

print(type(Vehicle2))
print(isinstance(Vehicle2, Vehicle))
print(isinstance(Vehicle2, Bus))
# Vehicle2.display_properties()
print(Vehicle2)







