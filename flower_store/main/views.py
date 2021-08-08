from . import main_blueprint
from flask import render_template, request, redirect, url_for, session
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

    result = db.session.execute(sql, {"id": id})
    flower = result.fetchone()

    return render_template('main/single_flower.html', flower=flower, id=id)


@main_blueprint.route('/shoppingcart')
@login_required
def shoppingcart():
    user_id = session["user_id"]
    cart_sql = ("SELECT shoppingcart.id, shoppingcart_item.quantity, flower.*, shoppingcart_item.quantity*flower.price as TOTAL_PRICE FROM shoppingcart, shoppingcart_item, flower WHERE shoppingcart.flower_user_id=:user_id AND shoppingcart.status_id=1"
    "AND shoppingcart_item.shoppingcart_id=shoppingcart.id AND shoppingcart_item.flower_id=flower.id;")

    aggregate_sql = ("SELECT SUM(shoppingcart_item.quantity*flower.price) as TOTAL, COUNT(flower.id) as QUANTITY, SUM(shoppingcart_item.quantity) as QUANTITY_total "
    "FROM shoppingcart, shoppingcart_item, flower "
    "WHERE shoppingcart.flower_user_id=1 AND shoppingcart.status_id=1 "
    "AND shoppingcart_item.shoppingcart_id=shoppingcart.id AND shoppingcart_item.flower_id=flower.id;")

    shoppingcart_result = db.session.execute(cart_sql, {"user_id": user_id}).fetchall()
    aggregate_result = db.session.execute(aggregate_sql).fetchone()
    return render_template('main/shoppingcart.html', cart=shoppingcart_result, aggregate=aggregate_result)


@main_blueprint.route('/add_to_cart', methods=["POST"])
def add_to_cart():

    return "kissa"
