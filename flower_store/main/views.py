from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app
from flower_store import db
from flower_store import login_required

@main_blueprint.route('/')
def index():  
   
    # return render_template('main/index.html')
    return redirect('/main_page')

@main_blueprint.route('/main_page')
def home():  
   
    # return render_template('main/index.html')
    return render_template('main/main_page.html')

@main_blueprint.route("/messages")
def messages():
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    return render_template("main/messages.html", count=len(messages), messages=messages)

@main_blueprint.route("/flowers")
def all_flowers():
    result = db.session.execute("SELECT * FROM flower;")
    flowers = result.fetchall()

    return render_template('main/flowers.html', flowers=flowers)

@main_blueprint.route("/flower/<int:id>")
@login_required
def single_flower(id):
    sql = "SELECT flower.*, inventory.* FROM flower INNER JOIN inventory ON flower.id=:id AND inventory.flower_id=flower.id;"
    
    result = db.session.execute(sql, {"id":id})
    flower = result.fetchone()   

    return render_template('main/single_flower.html', flower=flower, id=id)

@main_blueprint.route('/add/', methods=["POST"])

@main_blueprint.route('/shoppingcart')
def shoppingcart():

    return render_template('main/shoppingcart.html')
