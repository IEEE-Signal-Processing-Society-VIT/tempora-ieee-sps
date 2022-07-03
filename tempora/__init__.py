from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tempora.config import Config

db=SQLAlchemy()

def create_app(configClass=Config):
    app=Flask(__name__, template_folder='templates')
    app.config.from_object(configClass)
    db.init_app(app)

    #adding blueprints

    with app.app_context():
        db.create_all()
        
    return app
