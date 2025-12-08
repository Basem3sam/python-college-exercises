# Exercise 3: Validate Phone Numbers using Regular Expressions
import re

def validate_phone(phone):
    # Patterns with optional dashes: +1-555-1234 or 123-456-7890
    pattern = r'^(\+\d{1,3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
    return re.match(pattern, phone) is not None

# Test cases
test_numbers = ["+1-555-1234", "123-456-7890", "5551234", "12-345-6789"]
print("=== Phone Number Validation ===")
for number in test_numbers:
    print(f"{number}: {validate_phone(number)}")