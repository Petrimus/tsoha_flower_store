from . import auth_blueprint
from flask import render_template, request, redirect, url_for, current_app, session
from flower_store import db
from werkzeug.security import check_password_hash, generate_password_hash


@auth_blueprint.route('/login')
def login_form():

    return render_template('auth/login.html', error_message="")


@auth_blueprint.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if (not username or not password):
        return render_template('auth/login.html', error_message="You must give username (email) and password")

    sql = "SELECT id, password FROM flower_user WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return render_template('auth/login.html', error_message="Username or password incorrect")
    else:
        hash_value = user.password

    # if check_password_hash(hash_value, password):
    if (user.password == password):
        session["username"] = username
        session["user_id"] = user.id
        ses_id = create_shoppingcart(user.id)
        print(ses_id)
        session["shoppingcart_id"] = ses_id
        return redirect("/")
    else:
        return render_template('auth/login.html', error_message="Username or password incorrect")


@auth_blueprint.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    del session["shoppingcart_id"]
    return redirect("/")


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

    hash_value =  password # generate_password_hash(password)
    user_sql = "INSERT INTO flower_user (first_name, last_name, user_email, password) VALUES (:firstname, :lastname, :email, :password) RETURNING id;"
    saved_user = db.session.execute(user_sql, {
                                    "firstname": firstname, "lastname": lastname, "email": email, "password": hash_value})
    last_inserted_id = saved_user.fetchone()[0]
    adress_sql = "INSERT INTO adress (street_and_nro, postal_code, city, flower_user_id) VALUES (:adress, :postalcode, :city, :flower_user_id);"
    db.session.execute(adress_sql, {
                       "adress": adress, "postalcode": postalcode, "city": city, "flower_user_id": last_inserted_id})
    db.session.commit()

    return redirect('/')


def create_shoppingcart(user_id):    
    get_shoppingcart_sql = "SELECT * FROM shoppingcart WHERE flower_user_id=:id"
    cart = db.session.execute(get_shoppingcart_sql, {"id": user_id}).fetchone()

    insert_sql = "INSERT INTO shoppingcart (status_id, flower_user_id)",
    "select status_id, shoppingcart_status.id"
    "from ( values('open', {id})) as data(status_text, flower_user_id)",
    "join shoppingcart_status on shoppingcart_status.status_text = data.status_text RETURNING id;"

    if (not cart):
        sc_id = db.session.execute(insert_sql)
        db.session.commit()
        sc_sql =  "SELECT id FROM shoppingcart WHERE flower_user_id=:id"
        cart = db.session.execute(sc_sql, {"id": sc_id}).fetcone()
    
    return cart.id
