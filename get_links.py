import requests
from bs4 import BeautifulSoup


url = 'https://www.isystematic.com.pk/press-release/'
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')

links = [a.get('href') for a in soup.find_all('a', href=True)]
print(links)
