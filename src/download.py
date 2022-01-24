import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.time()

req = urllib.request.urlopen('http://www.example.com')

t1 = time.time()

print(f'Total time to fetch page: {t1 - t0} Seconds')

soup = BeautifulSoup(req.read(), 'html.parser')

for link in soup.find_all('a'):
  print(link.get('href'))

t2 = time.time()

print(f'Total execution time: {t2 - t1} Seconds')

# Total time to fetch page: 0.4270939826965332 Seconds
# https://www.iana.org/domains/example
# Total execution time: 0.0015649795532226562 Seconds
