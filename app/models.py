from app import db
from datetime import datetime

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), unique=False, nullable=False)
    price = db.Column(db.Integer(), unique=False, nullable=False)
    rent = db.Column(db.Integer(), unique=False, nullable=False)
    rooms = db.Column(db.Integer(), unique=False, nullable=False)
    taxes = db.Column(db.Integer(), unique=False, nullable=False)
    date_made = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    profit = db.Column(db.Integer(), unique=False, nullable=False)

    def __repr__(self):
        return f"House('{self.address}', '{self.price}', '{self.profit}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.Integer(), nullable=False)
    image_file = db.Column(db.Integer(), nullable=False, default='default.jpg')
    homes = db.Relationship('House', backref='username', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
