import os
import babel
from flask import Flask, render_template, redirect, session, flash, url_for
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from babel.dates import format_datetime

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.ProductionConfig')
    app.config.from_object(CONFIG_TYPE)
    app.secret_key = getenv("SECRET_KEY")
    db.init_app(app)
    register_blueprints(app)
    app.jinja_env.filters['datetime'] = format_datetime

    return app


def register_blueprints(app):
    from flower_store.auth import auth_blueprint
    from flower_store.main import main_blueprint
    from flower_store.admin import admin_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)


def initialize_extensions(app):
    pass


def register_error_handlers(app):
    pass


def configure_logging(app):
    pass


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('auth.login'))

    return wrap

def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    elif format == 'short':
        format="EE dd.MM.y"
    return babel.dates.format_datetime(value, format)   
