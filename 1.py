from urllib.request import urlopen 
html = urlopen('http://pythonscraping.com/pages/pagel.html') 
print(html.read())