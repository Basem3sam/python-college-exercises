# Exercise 2: Using map() and filter() to get squares of odd numbers

def square_odd_numbers(numbers):
  # Filter for odd numbers, then map to their squares
  odd_numbers = filter(lambda x: x % 2 != 0, numbers)
  squared = map(lambda x: x ** 2, odd_numbers)
  
  return list(squared)

test_list = [1, 2, 3, 4, 5]

print("=== Testing square_odd_numbers function: ===")
result = square_odd_numbers(test_list)

print(f"Input:  {test_list}")
print(f"Output: {result}")