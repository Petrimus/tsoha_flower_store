from . import auth_blueprint
from flask import render_template, request, redirect, url_for, current_app
from flower_store import db
from werkzeug.security import check_password_hash, generate_password_hash


@auth_blueprint.route('/login')
def login():

    return render_template('auth/login.html')


@auth_blueprint.route('/signup')
def signup_form():

    return render_template('auth/signup.html')


@auth_blueprint.route('/signup_result', methods=["POST"])
def signup_result():
    firstname = request.form["signup_firstname"]
    lastname = request.form["signup_lastname"]
    adress = request.form["signup_adress"]
    city = request.form["signup_city"]
    postalcode = request.form["signup_postalcode"]
    email = request.form["signup_email"]
    password = request.form["signup_password"]

    if (not firstname or not lastname or not adress or not city or not postalcode or not email or not password):
        return "One of fields is empty", 400

    if (len(password) < 8 or len(password) > 24):
        return "Password is invalid", 400

    sql = "SELECT * FROM flower_user where user_email=:email"
    result = db.session.execute(sql, {"email": email})
    users = result.fetchall()
    if (len(users) > 0):
        return "email already exists", 400

    hash_value = generate_password_hash(password)
    user_sql = "INSERT INTO flower_user (first_name, last_name, user_email, password) VALUES (:firstname, :lastname, :email, :password) RETURNING id;"   
    saved_user = db.session.execute(user_sql, {"firstname": firstname, "lastname": lastname, "email": email, "password": hash_value} )
    last_inserted_id = saved_user.fetchone()[0]
    adress_sql = "INSERT INTO adress (street_and_nro, postal_code, city, flower_user_id) VALUES (:adress, :postalcode, :city, :flower_user_id);"
    db.session.execute(adress_sql, {"adress":adress, "postalcode": postalcode, "city": city, "flower_user_id": last_inserted_id})
    db.session.commit()

    return redirect('/')
