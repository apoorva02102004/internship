from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    # Abstract method (must be implemented by child classes)
    @abstractmethod
    def sound(self):
        pass

    # Normal method (common for all animals)
    def sleep(self):
        print("This animal is sleeping...")


# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Bark")


# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Meow")


# Child Class 3
class Cow(Animal):
    def sound(self):
        print("Moo")


# Creating Objects
dog = Dog()
cat = Cat()
cow = Cow()

# Calling Methods
dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()
