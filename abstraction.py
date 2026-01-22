# Scenario:
# Design an abstract payment system where different payment methods can be implemented.
# Requirements:
# Create an abstract base class Payment with abstract method process_payment(amount)
# Create concrete classes: CreditCardPayment and PayPalPayment that inherit from Payment
# Each concrete class must implement process_payment() with different logic:
# CreditCardPayment : Print "Processing ${amount} via Credit Card"
# PayPalPayment : Print "Processing ${amount} via PayPal"
# Create a function make_payment(payment_method, amount) that accepts any Payment object
# Demonstrate that you cannot create an instance of the abstract Payment class directly

# ==== Solution

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# p1 = Payment()   # --> it is not possible

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing {amount} via credit card")
    
    
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing {amount} via paypal")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

p1 = CreditCardPayment()
p2 = PayPalPayment()

make_payment(p1, 200)
make_payment(p2, 300)



# ========================================================================

# Problem 3.2: Shape Calculator
# Scenario:
# Create an abstract Shape class for calculating area and perimeter of different shapes.
# Requirements:
# Create an abstract base class Shape with abstract methods: calculate_area() and calculate_perimeter()
# Create concrete classes: Rectangle and Circle that inherit from Shape
# Rectangle should have width and height attributes
# Circle should have radius attribute
# Each concrete class must implement both abstract methods with appropriate formulas
# Create a list of different shapes and calculate their areas and perimeters using polymorphism
# Demonstrate that Shape cannot be instantiated directly


# ===== Solution
from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.height * self.width) 
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

shapes = [
    Rectangle(10,20),
    Circle(7)
]

for shape in shapes:
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())