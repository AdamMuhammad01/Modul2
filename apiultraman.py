from bs4 import BeautifulSoup
import requests

# data = BeautifulSoup(open('digi.html', 'r'), 'html.parser')

# print(data.h1)
# print(data.h1.name)
# print(data.h1.text)
# print(data.h1.string)

url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')
strong = data.find_all('strong')
# print(data.find_all('strong'))
out = []
for i in strong:
    out.append(i.text)

# print(ultra)
ultra = out[2:36]
monster = out[37:110]
print('Ultraman:   ')
for i in ultra :
    print(i)

    
print('Monster:    ')
for i in monster:
    print( i)
# print(ultra)
# print(monster)
