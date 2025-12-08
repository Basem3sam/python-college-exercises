import math

class Shape:
  def area(self):
    return 0

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    
  def area(self):
    return math.pi * self.radius ** 2

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def area(self):
    return self.width * self.height

def print_shape_area(shape):
  area = shape.area()
  return f"Shape area: {area:.2f}"

# Create different shape objects
shapes = [ Shape(), Circle(5), Rectangle(4, 6) ]

# Testing polymorphism with shapes
print("=== Testing Shape Polymorphism ===")
for i in range(len(shapes)):
  print(f"Shape {i}: {print_shape_area(shapes[i])}\n")