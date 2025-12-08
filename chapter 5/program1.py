class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height
  
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return 2 * (self.width + self.height)

# Testing the Rectangle class
print("=== Testing Rectangle Class ===")
rect1 = Rectangle(5, 10)

print(f"Rectangle 1 (5x10):")
print(f"  Area: {rect1.area()}")
print(f"  Perimeter: {rect1.perimeter()}")
