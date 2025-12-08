# Exercise 3: Apply Multiple Transformations

nums = [1, 2, 3, 4, 5]

# Square each number, then add 10
transformed = list(map(lambda x: x**2 + 10, nums))

print("Original numbers:")
print(nums)
print("\nSquared + 10:")
print(transformed)
print("\nExpected Output: [11, 14, 19, 26, 35]")