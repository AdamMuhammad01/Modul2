'''
# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def beranda():
#     return render_template('home.html')

# if __name__ =='__main__':
#    app.run(debug=True, port=1945)
   
'''



from flask import Flask, jsonify, request
app = Flask(__name__)
import mysql.connector as mc
app = Flask(__name__)

dbku = mc.connect(
    host = 'localhost', user='root', passwd='363636',
    database = 'testing'
)
@app.route('/data', methods=['GET','POST'])
def data():
    
    if request.method == 'GET':
        x = dbku.cursor()
        sql = f'select * from datadiri where id = {no}'
        # x.execute('select * from datadiri ')
        hasil = x.fetchall()
        hasil = list(map(lambda i:{'id':i[0],'nama':i[1],'usia':i[2]},hasil))
        print (hasil)
        return jsonify(hasil)
    elif request.method == 'POST':
        body = request.json
        x = dbku.cursor()
        data = (body['nama'], body['usia'])
        sql = f'insert into datadiri (nama,usia) values {data}'
        x.execute(sql)
        dbku.commit()
        return 'POST'


@app.route('/data<int:no>', methods=['GET'])
def data(no):

if __name__ == '__main__':
    app.run(debug=True)