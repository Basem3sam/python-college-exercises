# Exercise 1: Validate email addresses using regular expressions
import re

def validate_email(email):
  # Pattern: starts with letters/numbers/underscore/dot, @ symbol, domain, .com/.org/.edu
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|edu)$'
  return re.match(pattern, email) is not None

test_emails = ["user@example.com", "bad-email", "test@domain.org"]

print("=== Testing validate_email function: ===")
for email in test_emails:
  is_valid = validate_email(email)
  print(f"Email: {email} => Valid: {is_valid}")