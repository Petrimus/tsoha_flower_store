from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app
from flower_store import db

@main_blueprint.route('/')
def index():  
   
    # return render_template('main/index.html')
    return render_template('main/home.html')

@main_blueprint.route("/messages")
def messages():
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    return render_template("main/messages.html", count=len(messages), messages=messages)
