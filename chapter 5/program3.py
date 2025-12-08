class Vehicle:
  def move(self):
    return "Vehicle is moving"

class Car(Vehicle):
  def move(self):
    return "Car is driving"

class Bike(Vehicle):
  def move(self):
    return "Bike is cycling"

# Create different vehicle objects
vehicles = [ Vehicle(), Car(), Bike(), Car(), Bike() ]

# Testing polymorphism
print("=== Testing Vehicle Hierarchy ===")
for i in range (len(vehicles)):
  print(f"Vehicle {i}: {vehicles[i].move()}\n")