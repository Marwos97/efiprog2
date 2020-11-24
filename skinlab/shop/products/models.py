from shop import db
from datetime import datetime


class Addskin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    float = db.Column(db.Numeric(), nullable=False)
    stock = db.Column(db.Integer(), default=1)
    
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),
        nullable=False)
    brand = db.relationship('Brand',
        backref=db.backref('brands', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    image = db.Column(db.String(150), nullable=False, default='image.jpg')
    
    def __repr__(self):
        return '<Post %r>' % self.title

    @staticmethod
    def get_by_collection(category_id):
        return Addskin.query.filter_by(category_id=category_id).first()


class Brand(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Category(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False, unique=True)


db.create_all()