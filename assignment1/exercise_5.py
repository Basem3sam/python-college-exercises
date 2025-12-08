# Exercise 5: Nested Map Transformation (Challenge 🌟)

marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]

# Increase each mark by 5% and round to nearest integer
incMarks = list(
            map(lambda row: list(
              map(lambda x: round(x * 1.05), row)
            ), marks)
          )

print("Original marks:")
print(marks)

print("\nMarks increased by 5% (rounded):")
print(incMarks)

print("\nExpected Output: [[47, 84, 74], [95, 63, 105], [92, 80, 97]]")