# Create a variable named data
data = 42  # Assign an integer value
print("1. Type after assigning integer:", type(data))

# Reassign data to a list
data = [1, 2, 3, 4]
print("2. Type after reassigning to list:", type(data))

# Reassign data to a function
def my_func():
  pass

data = my_func
print("3. Type after reassigning to function:", type(data))