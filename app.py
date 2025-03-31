from flask import Flask

app = Flask(__name__)


@app.route('/Hola/ida')
def Bienvenido():
    return 'Bienvenido'

@app.route('/Hola/vuelta')
def Adios():
    return 'Adios'