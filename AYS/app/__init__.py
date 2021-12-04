from flask import Flask

from .views.main import main

from extensions import *

def create_app():
    # Initialize app
    app = Flask(__name__)
    
    # Initialize config
    app.config.from_object('config.DevelopmentConfig')

    # Initialize extensions
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        # Register blueprints
        app.register_blueprint(main)
    
    return app