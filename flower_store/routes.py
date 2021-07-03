# from app import app
from flask import render_template


@app.route("/")
def index():
    return "Heipparallaa!"


@app.route("/page1")
def page1():
    return "Tämä on sivu 1"


@app.route("/page/<int:id>")
def page(id):
    return "Tämä on sivu "+str(id)


@app.route("/first_page")
def first():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")
