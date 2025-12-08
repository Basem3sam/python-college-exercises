class Employee:
  def __init__(self, name, employee_id, salary):
    self.name = name
    self.employee_id = employee_id
    self.salary = salary
  
  @classmethod
  def from_string(cls, employee_str):
    # Format: "Name, ID, Salary"
    name, emp_id, salary_str = employee_str.split(', ')
    salary = int(salary_str)
    return cls(name, emp_id, salary)
  
  def display_employee_info(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.employee_id}")
    print(f"Salary: ${self.salary:,}")

# Testing the Employee class
print("=== Testing Employee Class ===")

# Creating employee using standard constructor
emp1 = Employee("Alice Johnson", "E101", 60000)
print("Employee 1 (standard constructor):")
emp1.display_employee_info()

# Creating employee using class method
emp2_str = "Bob Smith, E205, 75000"
emp2 = Employee.from_string(emp2_str)
print("\nEmployee 2 (from_string constructor):")
emp2.display_employee_info()
