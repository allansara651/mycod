from urllib.request import urlopen 
from bs4 import BeautifulSoup 

#html = urlopen('https://www.httpvshttps.com/')
html = urlopen('https://cisco.com')
 
bs = BeautifulSoup(html.read(), 'html5lib')
print(bs) 