from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer)
    image_url = db.Column(db.String(200))

    def to_dict(self):
        return vars(self)

from faker import Faker
import random

def init_db():
    db.drop_all()
    db.create_all()
    fake = Faker()
    for _ in range(100):
        p = Product(
            name=fake.word().capitalize() + " " + fake.word(),
            category=random.choice(["Electronics", "Books", "Textiles"]),
            price=round(random.uniform(10, 999), 2),
            description=fake.text(),
            stock=random.randint(5, 100),
            image_url="https://via.placeholder.com/150"
        )
        db.session.add(p)
    db.session.commit()
