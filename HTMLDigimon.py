import pandas as pd
from bs4 import BeautifulSoup
import requests
# from flask import Flask, abort, jsonify, render_template
# server = Flask(__name__)

web = requests.get('http://digidb.io/digimon-list/')
data = BeautifulSoup(web.content,'html.parser')
title = ['Nomor', 'Digimon','Image','Stage','Type','Attribute','Memory','Equip Slots','HP','SP','Atk','Def','Int','Spd']
digi = []
new_digi = []

for i in data.find_all('td'):
    digi.append(i.text)

for i in range(0, len(digi),13):
    new_digi.append(digi[i:i+13])

gambar = []    #bikin img
for i in data.find_all('img'):
    gambar.append(i['src'])
gambar1 =gambar[2:243]

for i in range(len(gambar1)): #gabung img
    new_digi[i].insert(2,gambar1[i])

z = [] #bikin bentuk ke dict
for i in new_digi:
    z.append(dict(zip(title,i)))


#########################################

# df = pd.DataFrame(z).set_index('Nomer')

# ## home route

# @server.route('/')
# def home():
#     return render_template('home.html')

# @server.route('/cv')
# def cv():
#     return render_template('cv.html')

# @server.route('/digijs')
# def digijson():
#     return jsonify(z)

# @server.route('/digi')
# def digihtml():
#     return render_template('digi.html', data=df.to_html())


# #route untuk error 404
# @server.errorhandler(404)
# def notFound(error):
#     return render_template('error.html')

# if __name__ == ' __main__ ':
#     server.run(debug=True, host='localhost', port=4321)


