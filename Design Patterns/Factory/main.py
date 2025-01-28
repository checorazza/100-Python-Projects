from vehicle_factory import VehicleFactory

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
