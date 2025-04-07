from flask import Flask, url_for
from random import randint

app = Flask(__name__)


@app.route('/Hola/ida')


def Hola():
 url_hola = url_for("Hola")

 return f"""
 <a href="{url_hola}">Hola</a>
 """

@app.route('/Hola/vuelta')
def Adios():
    return 'Adios'

@app.route('/Hola/por-nombre/<string:nombre>') 
def sxn(nombre):
    return f'<p>Hola {nombre}<p>'

@app.route('/Tirar-dado/<int:caras>')
def dado(caras):
    n = randint(1,caras)
    return f'<p>Tire un dado de {caras} caras, salio {n}<p>'
