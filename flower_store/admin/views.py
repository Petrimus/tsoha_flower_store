from . import admin_blueprint
from flask import render_template, request, redirect, url_for, current_app, session, abort
from flower_store import db
from flower_store import login_required


@admin_blueprint.route("/admin/orders")
@login_required
def admin_orders():
  if not check_is_admin():    
    abort(403)
  
  return render_template('admin/index.html')


def check_is_admin():
  user_id = session["user_id"]

  return db.session.execute('SELECT is_admin FROM flower_user WHERE id={}'.format(user_id)).fetchone()[0]
 
