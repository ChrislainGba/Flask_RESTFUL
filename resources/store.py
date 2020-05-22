from flask_restful import Resource
from models.store import Store

class StoreResource(Resource):
    def get(self, name):
        store = Store.find_by_name(name)
        if store:
            return store.json()
        return {"message": "store not found"}, 404

    def post(self, name):
        store = Store.find_by_name(name)
        if store:
            return {"message": "store '{}'already there.".format(name)}, 400
        store = Store(name)
        try:
            store.save_to_db()
        except(e):
            print(e)
        return store.json()


    def delete(self, name):
        store = Store.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"Message":"store deleted"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in Store.query.all()]}
