from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app
from flower_store import db

@main_blueprint.route('/')
def index():  
    print(db) 
    try:
        print(db)
        db.session.execute("SELECT")
        print('connected to database')
    except Exception:  
        print('database not connected')
 
    result = db.session.execute("SELECT COUNT(*) FROM messages")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    # return render_template('main/index.html')
    return render_template('main/index.html' , count=count, messages=messages)
