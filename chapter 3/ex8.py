# Exercise 8: Decorator that logs function calls

import functools

def log_call(func):
    # Decorator that logs before and after calling a func
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

# Example decorated functions
@log_call
def add(a, b):
    # Add two nums
    return a + b

print("\nTest 1: add(5, 3)")
result = add(5, 3)