from abc import ABC, abstractmethod

#
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

#
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"

#
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")

# Use
def main():
    factory = VehicleFactory()

    car = factory.get_vehicle('car')
    print(car.drive())  # Output: Driving a car

    bike = factory.get_vehicle('bike')
    print(bike.drive())  # Output: Riding a bike

    truck = factory.get_vehicle('truck')
    print(truck.drive())  # Output: Driving a truck

if __name__ == "__main__":
    main()
