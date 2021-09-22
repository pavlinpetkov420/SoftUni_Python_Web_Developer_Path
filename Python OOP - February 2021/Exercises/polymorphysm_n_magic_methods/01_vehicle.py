from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    has_traveled = False
    conditioner_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = self.total_consumption(fuel_consumption)

    @staticmethod
    def total_consumption(fuel_consumption):
        return fuel_consumption + Car.conditioner_consumption

    def is_fuel_enough(self, distance):
        needed_fuel = self.fuel_consumption * distance
        return needed_fuel <= self.fuel_quantity

    def drive(self, distance):
        if self.is_fuel_enough(distance):
            self.fuel_quantity -= self.fuel_consumption * distance
            Car.has_traveled = True
            return
        Car.has_traveled = False

    def refuel(self, fuel):
        if Car.has_traveled:
            self.fuel_quantity += fuel


class Truck(Vehicle):
    has_traveled = False
    conditioner_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = self.total_consumption(fuel_consumption)

    @staticmethod
    def total_consumption(fuel_consumption):
        return fuel_consumption + Truck.conditioner_consumption

    def is_fuel_enough(self, distance):
        needed_fuel = self.fuel_consumption * distance
        return needed_fuel <= self.fuel_quantity

    def drive(self, distance):
        if self.is_fuel_enough(distance):
            self.fuel_quantity -= self.fuel_consumption * distance
            Car.has_traveled = True
            return
        Car.has_traveled = False

    def refuel(self, fuel):
        if Car.has_traveled:
            self.fuel_quantity += (fuel * 0.95)


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
