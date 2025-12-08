import numpy as np

# Create array from 1 to 10
arr = np.arange(1, 11)

# Calculate statistics
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std:.3f}")