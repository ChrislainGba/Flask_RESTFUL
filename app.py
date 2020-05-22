import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemResource, ItemList
from resources.store import StoreResource, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='Xl1'
api = Api(app)

iwt = JWT(app, authenticate, identity)


api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreResource, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#prevent runing when impoting this file
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)