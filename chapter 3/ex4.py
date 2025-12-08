# Exercise 4: create a closure that adds n to its argument.
def make_adder(n):
  # the return function "remembers" the value of n
  def adder(x):
    return x + n
  return adder

# Testing make_adder function
print("=== Testing make_adder function: ===")
add5 = make_adder(5)
result = add5(10)
print(f"add5(10) = {result}")  # Expected: 15

add10 = make_adder(10)
result = add10(10)
print(f"add10(10) = {result}")  # Expected: 20