class Point:
  # Using __slots__ to limit attributes and save memory.
  __slots__ = ['x', 'y']
  
  def __init__ (self, x, y):
      self.x = x
      self.y = y
  
  def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"

# Testing Point class with __slots__
print("=== Testing Point with __slots__ ===")
p1 = Point(2, 3)
print(f"Created point: {p1}")

# Try to add a new attribute (this should fail)
print("\nTrying to add a new attribute 'z':")
try:
    p.z = 5  # This shouldn't work
    print("Added z attribute:", p.z)
except AttributeError as e:
    print(f"Error: {e}")
    
# But it can be normally modified within defined slots :D