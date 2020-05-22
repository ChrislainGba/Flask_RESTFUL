
from db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('Store')

    def __init__(self, _id, name, price, store_id):
        self.id = _id,
        self.name = name,
        self.price = price
        self.store_id = store_id


     # getter method 
    def get_id(self): 
        return self.id
      
    # setter method 
    def set_id(self, x): 
        self.id = x 

    # getter method 
    def get_name(self): 
        return self.name
      
    # setter method 
    def set_name(self, x): 
        self.name = x 

    def get_price(self): 
        return self.price
      
    # setter method 
    def set_price(self, x): 
        self.price = x 
    
    def json(self):
        return {"id":self.id, "name":self.name, "price":self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        