from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    photo = db.Column(db.String())
    user_id = db.Column(db.String())
    date = db.Column(db.String(100))

    def __init__(self, name, price, description, photo, user_id, date):
        self.name = name
        self.price = price
        self.description = description
        self.photo = photo
        self.user_id = user_id
        self.date = date
