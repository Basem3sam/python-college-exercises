# Descriptor that only allows positive numbers
class Positive:
  def __init__(self, name):
    self.name = name  # store the attribute name

  def __get__(self, instance, owner):
    # Get value from instance dictionary, default to 0
    return instance.__dict__.get(self.name, 0)

  def __set__(self, instance, value):
    # Only allow 0 or positive values
    if value < 0:
      raise ValueError(f"{self.name} cannot be negative.")
    instance.__dict__[self.name] = value

# BankAccount class using the Positive descriptor
class BankAccount:
  balance = Positive("balance")  # apply descriptor

  def __init__(self, balance=0):
    self.balance = balance  # uses the descriptor __set__

# Test it out
print("=== Testing Positive Descriptor ===")

# Create account with positive balance
account = BankAccount(100)
print(f"Starting balance: ${account.balance}")

# Try to set negative balance (should fail)
try:
  account.balance = -50  # should raise ValueError
except ValueError as e:
  print(e)  # "balance cannot be negative."