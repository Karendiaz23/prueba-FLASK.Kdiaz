from flask import Flask

app = Flask(__name__)

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



