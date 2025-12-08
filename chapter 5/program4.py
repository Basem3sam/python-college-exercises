class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __sub__(self, other):
    # Vector subtraction
    return Vector(self.x - other.x, self.y - other.y)
  
  def __mul__(self, other):
    # Dot product: x1*x2 + y1*y2
    return self.x * other.x + self.y * other.y
  
  def __str__(self):
    return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Testing Vector operations
print("=== Testing Vector Class with Operator Overloading ===")
print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Test subtraction
result_sub = v1 - v2
print(f"\nv1 - v2 = { result_sub }")

# Test dot product
result_dot = v1 * v2
print(f"v1 · v2 (dot product) = { result_sub }")
