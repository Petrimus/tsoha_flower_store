from . import auth_blueprint
from flask import render_template, request, redirect, url_for, current_app

@auth_blueprint.route('/login')
def login():  
   
    return render_template('auth/login.html')

@auth_blueprint.route('/signup')
def signup():   
   
    return render_template('auth/signup.html')

@auth_blueprint.route('/auth/signup_result', methods=["POST"])
def result():
    firstname = request.form["signup_firstname"]
    lastname = request.form["signup_lastname"]
    adress = request.form["signup_adress"]
    city = request.form["signup_city"]
    postalcode = request.form["signup_postalcode"]
    email = request.form["signup_email"]
    