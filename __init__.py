# Importing packages
###from socket import socket
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# create_app function is used to init our flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from models import Users

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app