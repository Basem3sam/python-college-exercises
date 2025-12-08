# Exercise 2: Extract hashtags from a given text using regular expressions
import re

def extract_hashtags(text):
  # Extracts hashtags from the given text
  pattern = r'#\w+'
  return re.findall(pattern, text)

text = "#Python and #AI are great!"
hashtags = extract_hashtags(text)

print("=== Extracted Hashtags: ===")
print(f"Text: {text}")
print(f"Hashtags: {hashtags}")