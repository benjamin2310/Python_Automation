from itertools import count
from bs4 import BeautifulSoup
import requests
from sklearn.metrics import confusion_matrix
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div',class_='col-lg-4 col-md-6 mb-4')
for item in items:
    itemName = item.find('h4', class_='card-title').text
    itemPrice = item.find('h5').text.strip('\n')
    print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName)
    count += 1