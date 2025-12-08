import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> tags with href
links = soup.find_all('a', href=True)

for link in links:
  print(link['href'])