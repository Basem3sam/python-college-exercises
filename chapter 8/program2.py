import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Mohamed', 'Amina', 'Omar'],
    'Age': [20, 22, 21, 23, 20],
    'Score': [85, 78, 92, 88, 75]
})

# Filter students with score > 80
filtered = df[df['Score'] > 80]
print(filtered)