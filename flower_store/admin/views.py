from . import admin_blueprint
from flask import render_template, request, redirect, url_for, current_app, session, abort
from flower_store import db
from flower_store import login_required
from flower_store.admin import services


@admin_blueprint.route("/admin/orders")
@login_required
def admin_orders():
  if not services.check_is_admin():    
    abort(403)

  orders = services.get_orders()
  
  return render_template('admin/admin_main.html', orders=orders)



 
