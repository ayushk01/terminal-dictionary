import requests
import sys
from bs4 import BeautifulSoup as bs

res = requests.get('https://www.dictionary.com/browse/{}'.format(sys.argv[1]))

soup = bs(res.text, 'html.parser')

data = soup.findAll(True, {"class": ["css-pnw38j", "e1hk9ate4"]})

try:
    for string in data[0].strings:
        print(string)
except:
    print('Nothing Found!')
