# Exercise 6: Extract Dates from a String using Regular Expressions
import re

def extract_dates(text):
  # Extracts dates in YYYY-MM-DD format.
  
  pattern = r'\d{4}-\d{2}-\d{2}'
  return re.findall(pattern, text)

text = "The events are 2025-09-15, 2024-01-01, and 2023-12-31."
dates = extract_dates(text)

print("=== Testing extract_dates function: ===")
print(f"Text: {text}")
print(f"Extracted Dates: {dates}")