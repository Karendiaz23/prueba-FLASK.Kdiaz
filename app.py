from flask import Flask , url_for
import sqlite3 


app = Flask(__name__)
db =None


def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}



def abrirConexion():
    return sqlite3.connect("instace/datos.sqlite") 
    db.row_factory =dict_factory

def cerrarConexion():
  global db
  db.close() 
  db = None


@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
   AbrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT id, usuario, email, telefono, direccion FROM usuarios WHERE id = ?; ", (id,))
   res = cursor.fetchone()
   CerrarConexion
   usuario = None
   email = None
   telefono = None
   direccion = None
   if res != None:
       usuario = res['usuario']
       email = res['email']
       telefono = res['telefono']
       direccion = res['direccion']
   return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)



@app.route("/test-db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    res =cursor.execute("SELECT COUNT(*)AS cant from usuarios;")
    res =cursor.fethome()
    resgitros = res ["cant"]
    cerrarConexion()
    return f"hay{resgitros}registros en la tabla de usuarios"


@app.route("testdb")
def testdb():
    return


@app.route("/")
def main ():
    return  ""
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras =6)
    url_logo = url_logo("static", filename ="gatito.jgp")

    return f"""

    <a href="{url_hola}">hola</a>
    <br>
    <a href="{url_for("bye")}">chau</a>
    <br>
    <a href ="{url_logo}">logo</a>
    <br>
    <a href="{url_dado}">dado</a>

    """


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chau")
def bye_world():
    return "<p>chau,world</p>"

@app.route("/saludar/por-nombre/<string:nombre>")
def sxn(nombre):
    return "<p>hola{nombre}</p>"


@app.route("/sumar/<int:n1>/<int:n2>")
def sum(n1,n2):
    s= n1 + n2
    return f"<p>{n1} + {n2} = {s}</p>"

@app.route("/tirar-dados/<int:caras>")
def dado(caras):
    from random import randint
    n=randint(1,caras)
    return f"<p>tire un dado de{caras} caras , salio {n}</p>"



