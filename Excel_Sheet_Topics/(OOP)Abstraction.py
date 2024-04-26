from abc import ABC, abstractmethod
import math

# Define abstract base class (ABC) for Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by subclasses

# Concrete subclass Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Concrete subclass Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate area of any shape (accepts Shape object)
def calculate_area(shape):
    return shape.area()

# Creating instances of Circle and Rectangle
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# Using the same function with different shapes
print("Area of Circle:", calculate_area(my_circle))        # Output: Area of Circle: 78.53981633974483
print("Area of Rectangle:", calculate_area(my_rectangle))  # Output: Area of Rectangle: 24
