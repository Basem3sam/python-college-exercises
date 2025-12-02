# Exercise 6: Normalize Numbers Between 0 and 1

nums = [10, 20, 30, 40, 50]

# Find min and max values
minVal = min(nums)
maxVal = max(nums)

# Formula: (x - min) / (max - min)
normalized = list(map(lambda x: (x - minVal) / (maxVal - minVal), nums))

print("Original numbers:")
print(nums)
print(f"\nMin value: {minVal}")
print(f"Max value: {maxVal}")
print("\nNormalized (0 to 1):")
print(normalized)