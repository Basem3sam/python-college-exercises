from bs4 import BeautifulSoup

html = """
<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Alice</td><td>25</td></tr>
<tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find all rows
rows = soup.find_all('tr')

for row in rows:
  cells = row.find_all(['th', 'td'])
  data = [cell.text for cell in cells]
  print(data)