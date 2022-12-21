import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from recources.user import UserRegister, UserLogin
from recources.item import Item, ItemList


load_dotenv()


app = Flask(__name__)
api = Api(app)
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy()
jwt = JWTManager(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')


if __name__ == "__main__":
    app.run(debug=True)