from . import main_blueprint
from flask import render_template, request, redirect, url_for, session, abort
from flower_store import db
from flower_store import login_required


@main_blueprint.route('/')
def index():

    return redirect('/main_page')


@main_blueprint.route('/main_page')
def home():

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


@main_blueprint.route("/flower/<int:id>", methods=["GET", "POST"])
@login_required
def single_flower(id):
    cart_id = session["shoppingcart_id"]   

    message = ""
    if request.method == 'POST':
        flower_name = request.form["flower_name"]
        csrf_token = request.form["csrf_token"]
        shoppingcart_id = session["shoppingcart_id"]
        result = db.session.execute(
            "SELECT id FROM shoppingcart_item WHERE flower_id={} AND shoppingcart_id={};".format(id, cart_id))

        if not result.fetchone():
            db.session.execute(
                "INSERT INTO shoppingcart_item (flower_id, shoppingcart_id) VALUES ({}, {});".format(id, shoppingcart_id))
            db.session.commit()
            message = "{} added to the shopping cart".format(flower_name)

    single_sql = ("SELECT flower.*, inventory.quantity, "
                  "(SELECT COUNT(id) AS selected FROM shoppingcart_item WHERE shoppingcart_item.flower_id=:flower_id "
                  "AND shoppingcart_item.shoppingcart_id=:shoppingcart_id) "
                  "FROM flower INNER JOIN inventory ON flower.id=:flower_id AND inventory.flower_id=:flower_id;")

    result = db.session.execute(
        single_sql, {"flower_id": id, "shoppingcart_id": cart_id})
    flower = result.fetchone()

    if not flower:
        abort(404)

    return render_template('main/single_flower.html', flower=flower, id=id, cart_id=cart_id, message=message)


@main_blueprint.route("/shoppingcart")
@login_required
def shoppingcart():
    cart_id = session["shoppingcart_id"]
    return render_template('main/shoppingcart.html', cart=get_cart_info(cart_id), aggregate=get_aggregate_total(cart_id), cart_id=cart_id)


@main_blueprint.route("/shoppingcart/order", methods=["POST"])
@login_required
def place_order():
    cart_id = request.form["order_id"]
    csrf_token = request.form["csrf_token"]
    user_id = session["user_id"]

    order_sql = (
        "UPDATE shoppingcart SET status_id=2, modified_at=CURRENT_TIMESTAMP WHERE shoppingcart.id =:cart_id;")
    db.session.execute(order_sql, {"cart_id": cart_id})
    db.session.commit()
    insert_sql = "INSERT INTO shoppingcart (status_id, flower_user_id)  values (1, {}) RETURNING id;".format(
        user_id)
    result = db.session.execute(insert_sql)
    new_cart_id = result.fetchone()[0]
    session["shoppingcart_id"] = new_cart_id
    db.session.commit()

    return redirect('/shoppingcart')


@main_blueprint.route("/shoppingcart/update_shopping_cart", methods=["post"])
@login_required
def update_shoppingcart():
    shoppingcart_id = request.form["shopping_cart_id"]
    # csrf_token = request.form["csrf_token"]

    for flower_id, quant in request.form.items():

        if flower_id.isdigit():
            print('flower_id ' + flower_id)
            print('quantity ' + quant)
            print('shoppingcart_id' + shoppingcart_id)
            update_sql = ("UPDATE shoppingcart_item "
                          "SET quantity=:quantity, modified_at=CURRENT_TIMESTAMP "
                          "WHERE shoppingcart_item.flower_id=:flower_id AND shoppingcart_item.shoppingcart_id=:cart_id;")

            db.session.execute(
                update_sql, {"quantity": quant, "flower_id": flower_id, "cart_id": shoppingcart_id})
            db.session.commit()

    return redirect('/shoppingcart')


@main_blueprint.route("/shoppingcart/remove/<int:flower_id>/<int:cart_id>", methods=["GET"])
@login_required
def remove_item_from_cart(flower_id, cart_id):
    db.session.execute(
        "DELETE FROM shoppingcart_item WHERE shoppingcart_item.flower_id={} AND shoppingcart_item.shoppingcart_id={};".format(flower_id, cart_id))
    db.session.commit()

    return redirect('/shoppingcart')


@main_blueprint.route("/flower/search", methods=["POST"])
def nav_search():

    return "kissa"


@main_blueprint.route("/orders")
@login_required
def order_list():
    user_id = session["user_id"]

    order_sql = ("SELECT shoppingcart.id AS cart_id, shoppingcart.status_id, shoppingcart.modified_at, "
                 "shoppingcart_status.status_text AS status, shoppingcart_status.id AS status_id "
                 "FROM shoppingcart, shoppingcart_status WHERE shoppingcart.status_id=shoppingcart_status.id "
                 "AND shoppingcart.flower_user_id=:user_id AND shoppingcart.status_id > 1 "
                 "ORDER BY shoppingcart.status_id;")

    order_list = db.session.execute(order_sql, {"user_id": user_id}).fetchall()

    return render_template("main/orders.html", orders=order_list)


@main_blueprint.route("/order/<int:cart_id>")
def single_order(cart_id):

    return render_template("main/order.html", cart=get_cart_info(cart_id), aggregate=get_aggregate_total(cart_id), cart_id=cart_id)


def get_aggregate_total(cart_id):
    user_id = session["user_id"]

    aggregate_sql = ("SELECT SUM(shoppingcart_item.quantity * flower.price) as TOTAL, shoppingcart.modified_at, "
                     "COUNT(flower.id) as QUANTITY, SUM(shoppingcart_item.quantity) as QUANTITY_total "
                     "FROM shoppingcart, shoppingcart_item, flower "
                     "WHERE shoppingcart.flower_user_id=:user_id AND shoppingcart.status_id=1 "
                     "AND shoppingcart_item.shoppingcart_id=shoppingcart.id AND shoppingcart_item.flower_id=flower.id GROUP BY shoppingcart.modified_at;")

    return db.session.execute(
        aggregate_sql, {"shoppingcart_id": cart_id, "user_id": user_id}).fetchone()


def get_cart_info(cart_id):

    cart_sql = ("SELECT shoppingcart.id AS cart_id, shoppingcart_item.quantity, flower.*, shoppingcart_item.quantity*flower.price as TOTAL_PRICE, "
                "inventory.quantity AS stock FROM shoppingcart, shoppingcart_item, flower, inventory WHERE shoppingcart.id=:cart_id "
                "AND shoppingcart_item.shoppingcart_id=shoppingcart.id AND shoppingcart_item.flower_id=flower.id "
                "AND inventory.flower_id=flower.id;")

    result = db.session.execute(
        cart_sql, {"cart_id": cart_id}).fetchall()
    
    print(result)
    return result
