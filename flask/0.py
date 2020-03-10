from flask import Flask, jsonify , render_template

server = Flask(__name__)

# #home route
@server.route('/')
def home():
    return '<h1>Halo semuanya</h1>'

#render html
@server.route('/')
def data():
    return render_template('html.html')

#send data from flask, render html
@server.route('/')
def datas():
    nama ="andi"
    kota = "jakarta"
    return render_template(
        'data.html',
        data = {'name':nama,'city':kota}
    )


karyawan = [
    {"id":1,"nama":"andi","usia":20,"kota":"Jakarta"},
    {"id":2,"nama":"adi","usia":23,"kota":"Jakarta"},
    {"id":3,"nama":"anda","usia":24,"kota":"Jakarta"},
    {"id":4,"nama":"aldo","usia":23,"kota":"Jakarta"},
    {"id":5,"nama":"adri","usia":22,"kota":"Jakarta"},
    {"id":6,"nama":"abdi","usia":21,"kota":"Jakarta"},
    {"id":7,"nama":"asmi","usia":21,"kota":"Jakarta"},
]

@server.route('/karyawan')
def karyawan():
    return jsonify(Employees)

@server.route('/karyawan/<int:id>')
def employees(id):
    return jsonify(Employees[id-1])

if __name__ == '__main__':
    server.run(
        debug = True,
        host = 'localhost',
        port = 1234
    )

if __name__ == '__main__' :
     server.run(debug = True)

     