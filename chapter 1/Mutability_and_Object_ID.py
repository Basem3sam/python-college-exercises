# Create a list
my_list = [10, 20, 30]

# Check initial memory address
print("1. Memory address before append:", id(my_list))

# Modify the list by appending
my_list.append(40)

# Check memory address after modification  
print("2. Memory address after append:", id(my_list))

# Compare addresses
print("3. Same address?", id(my_list) == id(my_list))