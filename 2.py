from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen('https://www.httpvshttps.com/') 
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1) 