from . import admin_blueprint
from flask import render_template, request, redirect, url_for, current_app, session
from flower_store import db
from flower_store import login_required


@main_blueprint.route('/admin/orders')
@login_required
def admin_orders():
  if not check_is_admin():
    
    return redirect('/main_page')


def check_is_admin():
  user_id = session["user_id"]

  is_admin = db.session.execute('SELECT is_admin FROM flower_user WHERE id={}'.format(user_id)).fetchone()
  
  return True if not is_admin else False

