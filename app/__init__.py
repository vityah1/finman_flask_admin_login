from flask import Flask
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
from flask_cors import CORS
import os, config

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# print("import ok")

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "main.login"
admin = Admin(name="finman", template_mode="bootstrap4")

# Фабрика приложения
def create_app(config):
    # создание экземпляра приложения
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config.from_object(config)
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    # admin.init_app()

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth

    app.register_blueprint(auth)

    from .api import api_bp
    from .api import api_crud_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(api_crud_bp)
    # app.register_blueprint(auth_bp)
    # db.create_all()
    admin.init_app(app)

    # Add the admin panel
    from app.admin import bp as admin_bp

    app.register_blueprint(admin_bp)

    # from .admin import main as admin_blueprint
    # app.register_blueprint(admin_blueprint)

    return app
