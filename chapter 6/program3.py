import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ali', 'Sara', 'Omar'],
    'Salary': [5000, 6000, 5500]
})

# Save to Excel
df.to_excel('employees.xlsx', index=False)

# Read from Excel
df_read = pd.read_excel('employees.xlsx')
print(df_read[['Name', 'Salary']])