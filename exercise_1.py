# Exercise 1: Transform and Clean Data

products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]

# Removing extra spaces and Converting to title case
cleaned_products = list(map(lambda x: x.strip().title(), products))

print("Original products:")
print(products)
print("\nCleaned products:")
print(cleaned_products)
print("\nExpected Output: ['Laptop', 'Phone', 'Tablet', 'Camera']")