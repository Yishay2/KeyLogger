from abc import ABC, abstractmethod
import math
from traceback import print_tb


# exercise 1
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
       return math.pi * (self.radius ** 2)


# exercise 2
class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):

    def process_payment(self, amount):
        print("The payment was done by credit card!")


class PayPalProcessor(PaymentProcessor):

    def process_payment(self, amount):
        print("The payment was done by paypal!")


# exercise 3
class Animal(ABC):

    def __init__(self, name, num_of_legs):
        self.name = name
        self.num_of_legs = num_of_legs

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def __init__(self, name, num_of_legs):
        super().__init__(name, num_of_legs)

    def speak(self):
        print("woaff woaff!")

    def move(self):
        print(f"{self.name} is moving!")

class Bird(Animal):

    def __init__(self, name, num_of_legs):
        super().__init__(name, num_of_legs)

    def speak(self):
        print("tziff tziff!")

    def move(self):
        print(f"{self.name} is moving!")


# exercise 4


# exercise 5



# exercise 6

class OnlineStore(ABC):

    pass

class Encryptor(ABC):

    def AES(self):
        pass

    def RSA(self):
        pass


class Employee(ABC):

    pass
