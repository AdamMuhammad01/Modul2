
# from flask import Flask, jsonify, request
# app = Flask(__name__)

import mysql.connector as mc
# app = Flask(__name__)

# dbku = mc.connect(
#     host = 'localhost', user='root', passwd='363636',
#     database = 'testing'
# )
# @app.route('/data', methods=['GET','POST'])
# def data():
    
#     if request.method == 'GET':
#         x = dbku.cursor()
#         x.execute('select * from datadiri ')
#         hasil = x.fetchall()
#         hasil = list(map(lambda i:{'id':i[0],'nama':i[1],'usia':i[2]},hasil))
#         print (hasil)
#         return jsonify(hasil)
#     elif request.method == 'POST':
#         return 'POST'

# if __name__ == '__main__':
#     app.run(debug=True)