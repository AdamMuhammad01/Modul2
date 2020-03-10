import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import requests


from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www2.2019seagames.com/countries/'
x = requests.get(url)
soup = BeautifulSoup(x.content,'html.parser')
b = soup.find_all('em')


c = []
for j in b:
    c.append(j.text)
negara = []
gold = []
country = c[:66:6]
emas = c[2:66:6]
negara.append(country)
gold.append(emas)
print(negara)
seventeen = np.array([0,3,38,2,145,7,24,57,72,0,58])

url = 'https://rs.2019seagames.com/RS2019/mobiapp/MedalTally'
y = requests.get(url)
d = BeautifulSoup(y.content,'html.parser')
e = d.find_all('small')
# print(e)
nineteen= []

for i in e:
    nineteen.append(i.text)
nineteen = nineteen[6::5]
print(nineteen)
nineteen = np.array([2,4,72,1,55,4,149,52,92,0,98])

persentase = []
for j in seventeen:
    b = j/406
    persentase.append(b)
# print(persentase)
    persentasee = []
for i in nineteen:
    asd = i/529
    persentasee.append(asd)

a = pd.DataFrame({
    '2017':[0,3,38,2,145,7,24,57,72,0,58],
    '2019':[2,4,72,1,55,4,149,52,92,0,98],
    'x':country
})

#bar chart

# plt.style.use('ggplot')
# plt.figure('GOLD MEDAL TALLY SEA GAMES 2017 & 2019',figsize=(16,8))
# plt.plot(a['x'],a['2017'],color='red')
# plt.plot(a['x'],a['2019'],color='green')
# plt.scatter(a['x'],a['2017'], marker='o', s=300, color='r', edgecolor='r',zorder=3)
# plt.scatter(a['x'],a['2019'], marker='o', s=300, color='g', edgecolor='r',zorder=3)
# plt.grid()
# plt.legend(['2017','2019'])
# plt.title('GOLD MEDAL TALLY SEA GAMES 2017 & 2019')
# plt.xticks(rotation=20)
# plt.show()


#pie chart

plt.style.use('ggplot')
plt.subplot(1,2,1)
plt.pie(persentase,colors=['blue','green','red','blue','brown','lightblue','blue','green','red','yellow','brown'],
        labels=country,startangle=90,textprops={'size':7,'color':'black'},autopct='%1.2f%%')
plt.title('GOLD % SEA GAMES 2017',fontdict={'family':'calibri','size':25,'color':'black'})
plt.show()

plt.subplot(1,2,2)
plt.pie(persentasee,colors=['blue','green','red','blue','brown','lightblue','blue','green','red','yellow','brown'],
        startangle=90,labels=country,textprops={'size':7,'color':'black'},autopct='%1.2f%%')
plt.title('GOLD % SEA GAMES 2019',fontdict={'family':'calibri','size':25,'color':'black'})
plt.show()
