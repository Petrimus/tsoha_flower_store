from flask import session
from flower_store import db

def check_is_admin():
  user_id = session["user_id"]

  return db.session.execute('SELECT is_admin FROM flower_user WHERE id={}'.format(user_id)).fetchone()[0]

def get_orders():
  all_orders_sql = ("SELECT shoppingcart.id AS cart_id, shoppingcart_status.status_text AS status, "
  "shoppingcart.modified_at, flower_user.last_name "
  "FROM shoppingcart JOIN flower_user ON flower_user.id=shoppingcart.flower_user_id "
  "JOIN shoppingcart_status ON shoppingcart.status_id=shoppingcart_status.id ORDER BY status;"
  )

  return db.session.execute(all_orders_sql).fetchall()

def get_users():
  users_sql = ("SELECT flower_user.id, flower_user.username, adress.street_and_nro, adress.city, "
  "COUNT(shoppingcart.id) AS count FROM flower_user "
  "LEFT JOIN adress ON adress.flower_user_id=flower_user.id "
  "LEFT JOIN shoppingcart ON flower_user.id=shoppingcart.flower_user_id AND "
  "shoppingcart.status_id>1 GROUP BY flower_user.id, adress.street_and_nro, adress.city;")

  return db.session.execute(users_sql).fetchall()

  