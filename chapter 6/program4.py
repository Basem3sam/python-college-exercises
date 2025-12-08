import csv
import json

# Read CSV and convert to list of dictionaries
people = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append({"Name": row['Name'], "Age": int(row['Age']), "City": row['City']})

# Write to JSON
output = {"people": people}
with open('output.json', 'w') as file:
    json.dump(output, file, indent=4)

print("Conversion complete!")
