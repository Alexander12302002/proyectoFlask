import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    peticion = requests.get("https://66084670a2a5dd477b14441c.mockapi.io/allproduct")
    return render_template('index.html', data=peticion.json())

@app.route("/views/abrigos")
def abrigos():
    return render_template('abrigos.html')

@app.route("/views/camisetas")
def camisetas():
    return render_template('camisetas.html')

@app.route("/views/carrito")
def carrito():
    return render_template('carrito.html')

@app.route("/views/pantalones")
def pantalones():
    return render_template('pantalones.html')



app.run()   