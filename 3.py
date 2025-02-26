from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen('https://www.httpvshttps.com/') 
bs = BeautifulSoup(html.read(), 'lxml')
print(bs) 