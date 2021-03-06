from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import Item


#Resource
class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', 
        type=str,
        required=True,
        help="This field can not be left blank!"
    )
    parser.add_argument('price', 
        type=float,
        required=True,
        help="This field can not be left blank!"
    )
    parser.add_argument('store_id', 
        type=int,
        required=True,
        help="Each item needs a store id!"
    )
    #@jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item.json()
        return {"message": "item daesn't exists"}, 404



    def post(self, name):
        if Item.find_by_name(name):
            return {'message':"An item with name '{}' already exsit.".format(name)}, 400
        data = ItemResource.parser.parse_args()
        item = Item(None, str(name), data['price'], data['store_id'])
        item.set_id(None)
        item.set_name(name)
        try:
            item.save_to_db()
        except() as e:
            print(e)
            return {"message":"an exception occurred inserting into DB"}, 500
        return item.json(), 201
        


    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()   
            return {'message': 'item deleted'}
        return {'message':"An item with name '{}' not exsit.".format(name)}, 400
    
    def put(self, name):
        #data = request.get_json()
        data = ItemResource.parser.parse_args()
        item = Item.find_by_name(name)
        if item is None:           
            item = Item(None, name, data['price'], data['store_id'])
            item.set_id(None)
            item.set_name(name)
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):  
        return {"items": list(map(lambda x: x.json(), Item.query.all()))}
