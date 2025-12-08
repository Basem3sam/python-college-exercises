# Exercise 1: Pure function to remove vowels from a string

def remove_vowels(text):
  # This is a pure function - no side effects
  vowels = "aeiouAEIOU"
  
  # Remove all vowels (a, e, i, o, u) from the input string.
  return ''.join(char for char in text if char not in vowels)


test_str = "Hello World"

print("=== Testing remove_vowels function: ===")
result = remove_vowels(test_str)
print(f"Input:  '{test_str}'")
print(f"Output: '{result}'")