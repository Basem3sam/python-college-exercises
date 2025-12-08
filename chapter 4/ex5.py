# Exercise 5: Find Duplicate Words in a String using Regular Expressions
import re

def find_duplicate_words(text):
  # Pattern: word followed by whitespace and the same word

  pattern = r'\b(\w+)\s+\1\b'
  matches = re.findall(pattern, text)
  
  full_matches = [f"{word} {word}" for word in matches]
  return full_matches

text = "This is is a test test"

duplicates = find_duplicate_words(text)

print("=== Testing find_duplicate_words function: ===")
print(f"Text: {text}")
print(f"Duplicates found: {duplicates}")