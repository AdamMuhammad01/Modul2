import requests
import urllib

# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url)
# print(data.json())
# print(type(data.json()))
#
# for i in data.json():
#     print(i['name'], 'di Jl.', i['address']['street'])




# klub = input('ketik nama klub : ')
# url = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
# data = requests.get(url)
# # print(data.json())
# # print(type(data.json()))
# players = data.json()['player']
# for player in players:
#     # print(player['dateBorn'])
#     print(f"{player['strPlayer']}, {player['strSigning']}, ({player['strPosition']})")





# url = 'http://quotes.rest/qod'
#
# data = requests.get(url)
# data = data.json()
# print(data)
# print(data['contents']['quotes'][0]['quotes'])





x = '&appid=db9f1a6efcb7688d27095903a80b70a6'
y = input('ketik nama kota: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={city name}'    #error
data = requests.get(url)
data = data.json()
print(data)
print(data['sys']['sunrise'])


# from datetime import datetime
# waktu = datetime.utcfromtimestamp(int(sunrise))
# print(waktu)

##########################################################homework

# 1. get api sportsdb, daftar pemainsuatu klub
# 2. input klub apa?
# 3. daftar pemain : nama, posisi, usia, negara
# save dalam bentuk excel,csv,json
# [{
#     "nama":"adam",
#     'posisi':"....",
#     "usia":"....",
#     "negara":"..."
# }

# ]

'''

klub = input('ketik nama klub : ')
url = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
data = requests.get(url)
# print(data.json())
# print(type(data.json()))
players = data.json()['player']
for player in players:
#      print(player['strPlayer'])
      print(f"{player['strPlayer']}, posisi :  {player['strPosition']}, negara :  {player['strNationality']}")  # error


'''
