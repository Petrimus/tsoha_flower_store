from . import db

class Floweruser(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  useremail = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.useremail}')"

class Flowers(db.Model):


class Order_details(db.Model):

class Order_items(db.Model):


class Inventory(db.Model):



class Cart(db.Model):

class Session(db.model):
  

# class Creditcard(db.model):