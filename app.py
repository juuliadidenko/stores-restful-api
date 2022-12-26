import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, UserLogin
from resources.item import Item, ItemList
from db import db
from models.item import ItemModel
from models.user import UserModel


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))






app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(basedir, 'data.db')
db.init_app(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'UserModel': UserModel,
        'ItemModel': ItemModel
    }


if __name__ == "__main__":
    app.run(debug=True)