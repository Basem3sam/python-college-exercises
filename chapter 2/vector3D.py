class Vector3D:
    # A class representing a 3D vector with x, y, and z components.    
    def __init__(self, x, y, z):
        # Initialize the vector with x, y, z components.
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        # Add two vectors components (+ op).
        return Vector3D(self.x + other.x, 
                        self.y + other.y, 
                        self.z + other.z)
    
    def __sub__(self, other):
        # Subtract two vectors components (- op).
        return Vector3D(self.x - other.x, 
                        self.y - other.y, 
                        self.z - other.z)
    
    def __mul__(self, other):
        # Calculate dot product of two vectors (* op).
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def __repr__(self):
        # Return a clear string representation of the vector.
        return f"Vector3D({self.x}, {self.y}, {self.z})"


# Testing the Vector3D class
print("=== Testing Vector3D Class ===")

# Create two vectors
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Test addition
v3 = v1 + v2
print(f"\nv1 + v2 = {v3}")

# Test subtraction
v4 = v1 - v2
print(f"v1 - v2 = {v4}")

# Test dot product
dot_product = v1 * v2
print(f"v1 · v2 (dot product) = {dot_product}")

"""" THATS A LOT :D """