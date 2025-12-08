from bs4 import BeautifulSoup
import csv

html = """
<ul>
<li>Apple</li>
<li>Banana</li>
<li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')

# Extract all fruits
fruits = [li.text for li in soup.find_all('li')]

# Save to CSV
with open('fruits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit'])  # Header
    for fruit in fruits:
        writer.writerow([fruit])

print("Data saved to fruits.csv")