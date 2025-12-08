# Exercise 8: Extract Programming Language Names from a String using Regular Expressions
import re

def extract_emails(text):
  # Extracts programming language names from text.
  
  pattern = r'\b(Python|Java|C\+\+|Ruby)\b'
  return re.findall(pattern, text)

text = "I know Python, Java, and C++ but not Ruby."
languages = extract_emails(text)

print("=== Testing extract_emails function: ===")
print(f"Text: {text}")
print(f"Extracted Languages: {languages}")