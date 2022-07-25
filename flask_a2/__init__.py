from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# App Configurations

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'flask_app.login'
migrate = Migrate()
manager = Manager()
bcrypt = Bcrypt()

def initialize_extensions(app):
    from .models import User, Post
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    manager.add_command('db', MigrateCommand)


def create_app(config_filename = None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = open("/run/secrets/my_secret", "r").read().strip()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    initialize_extensions(app)
    with app.app_context():
        db.create_all()
    from .routes import flask_app
    from . import models, routes
    app.register_blueprint(flask_app)
    return app

