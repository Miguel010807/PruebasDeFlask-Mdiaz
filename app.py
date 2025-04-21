from flask import Flask, render_template, url_for
import sqlite3
from random import randint


app = Flask(__name__)

db = None

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory

def cerrarConexion():
   global db
   db.close
   db.row_factory = dict_factory

@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios")
   res = cursor.fetchone
   registros = res["cant"]
   cerrarConexion()
   return f"hay {registros} registros en la tabla usuarios"

@app.route("/crear-usuario") #Esta pagina esta sin argumentos
def testCrear():
   nombre = "Tomi"
   email = "tomi@etec.uba.ar"
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SINSERT INTO usuarios (usuario, emial) VALUES (nombre, email)")
   res = cursor.fetchone
   registros = res["cant"]
   cerrarConexion()
   return f"hay {registros} registros en la tabla usuarios"

@app.route("/crear-usuario-arg/<string:nombre>/<string:email>") #este pagina esta con Argumentos( nombre y email)
def testCrearXArgu(nombre,email):
   abrirConexion()
   cursor = db.cursor()
   consulta = "INSERT INTO usuarios (usuario, email) VALUES (?, ?)"
   cursor.execute(consulta,(nombre, email))
   db.commit
   cerrarConexion()
   return f"hay un resgistro agregado( {nombre}, {email})"

@app.route('/Hola/ida')


def Hola():
 #         "Aca va el nombre del DEF"
 url_hola = url_for("Adios")

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


@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email FROM usuarios WHERE id = ?; ", (id,) )
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
       usuario= res["usuario"]
       email = res["email"]
    return render_template("datosjuntos.html", id=id, usuario=usuario, email=email)    







