from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Flower_user(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  useremail = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.useremail}')"

class Creditcard(db.model):
  id = db.Column(db.Integer, primary_key=True)
  experience_date = db.Column(db.Date, nullable=False)
  card_number = db.Column(db.Integer, nullable=False, unique=True)

class Flower(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  latin_name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.String(200), unique=True, nullable=False)
  price = db.Column(db.Float, nullable=False)
  created_at = db.Column(db.Date, nullable=False)


class Shoppingcart(db.Model):

class Shoppingcart_items(db.Model):

class Shoppingcart_status(db.Model):

class Inventory(db.Model):




