import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from db import db
from models import StoreModel
blp = Blueprint('Stores',__name__,description="Store operations")

@blp.route('/store/<int:store_id>')
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {'message':'Store has been deleted'}

@blp.route('/store')
class StoreList(MethodView):

    @blp.response(201,StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400,message='Store with this name already exists')
        except SQLAlchemyError:
            abort(500,message='Error occured during creating the store') 
        return store
