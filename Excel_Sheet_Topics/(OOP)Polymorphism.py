import math

class Shape:
    def area(self):
        pass  # Placeholder for subclasses to implement

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate area of any shape
def calculate_area(shape):
    return shape.area()

# Creating instances of Circle and Rectangle
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# Using the same function with different shapes
print("Area of Circle:", calculate_area(my_circle))        # Output: Area of Circle: 78.53981633974483
print("Area of Rectangle:", calculate_area(my_rectangle))  # Output: Area of Rectangle: 24
