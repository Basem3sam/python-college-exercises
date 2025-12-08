# Exercise 5: Higher-order function that applies a function twice
def apply_twice(func, value):
  # Apply the given function 'func' to 'value' two times.
  return func(func(value))

# Testing apply_twice function
print("=== Testing apply_twice function: ===")
result = apply_twice(lambda x: x + 1, 5)

print(f"apply_twice(lambda x: x + 1, 5) = {result}")
print("Explanation: 5 -> 6 -> 7")