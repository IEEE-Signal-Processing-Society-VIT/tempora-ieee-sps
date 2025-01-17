from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from tempora.config import Config

db=SQLAlchemy()
ma= Marshmallow()

def create_app(configClass=Config):
    app=Flask(__name__, template_folder='templates')
    app.config.from_object(configClass)
    db.init_app(app)
    app.static_folder = 'static'

    #adding blueprints
    from tempora.register.routes import register_blueprint
    app.register_blueprint(register_blueprint)
    
    from tempora.hompage.routes import homepage_blueprint
    app.register_blueprint(homepage_blueprint)

    # with app.app_context():
    #     db.create_all()
        
    return app

