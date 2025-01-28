from car import Car
from bike import Bike
from truck import Truck

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
