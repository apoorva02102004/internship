from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass


# Child class 1
class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started with a key or push button.")


# Child class 2
class Bike(Vehicle):
    
    def start_engine(self):
        print("Bike engine started with a self-start or kick.")


# Child class 3
class Bus(Vehicle):
    
    def start_engine(self):
        print("Bus engine started with a heavy-duty ignition system.")


# Creating objects
car = Car()
bike = Bike()
bus = Bus()

# Calling start_engine() method
car.start_engine()
bike.start_engine()
bus.start_engine()
