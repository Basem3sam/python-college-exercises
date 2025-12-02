# Exercise 2: Convert Temperatures (Celsius -> Fahrenheit)

celsius = [0, 10, 20, 30, 40]

# Formula: F = (9/5) * C + 32
fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))

print("Temperatures in Celsius:")
print(celsius)
print("\nTemperatures in Fahrenheit:")
print(fahrenheit)
print("\nExpected Output: [32.0, 50.0, 68.0, 86.0, 104.0]")