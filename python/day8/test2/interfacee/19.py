from abc import ABC, abstractmethod

# Interface IVehicle
class IVehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass


# Implementing IVehicle in Car class
class Car(IVehicle):
    
    def start_engine(self):
        print("Car engine started.")
        # Code to start the car engine

    def stop_engine(self):
        print("Car engine stopped.")
        # Code to stop the car engine


# Implementing IVehicle in Bike class
class Bike(IVehicle):
    
    def start_engine(self):
        print("Bike engine started.")
        # Code to start the bike engine

    def stop_engine(self):
        print("Bike engine stopped.")
        # Code to stop the bike engine


# Implementing IVehicle in Truck class
class Truck(IVehicle):
    
    def start_engine(self):
        print("Truck engine started.")
        # Code to start the truck engine

    def stop_engine(self):
        print("Truck engine stopped.")
        # Code to stop the truck engine


# Example Usage
if __name__ == "__main__":
    # Creating instances of each vehicle
    car = Car()
    bike = Bike()
    truck = Truck()

    # Starting and stopping engines for each vehicle
    car.start_engine()
    car.stop_engine()

    bike.start_engine()
    bike.stop_engine()

    truck.start_engine()
    truck.stop_engine()
