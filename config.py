import os

app_dir = os.path.abspath(os.path.dirname(__file__))
from func import cfg


class BaseConfig:
    # SECRET_KEY = os.environ.get("SECRET_KEY") or "A SECRET KEY"
    SECRET_KEY = cfg.get("SECRET_KEY", "A SECRET KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### настройка Flask-Mail #####
    MAIL_SERVER = cfg.get("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "YOU_MAIL@gmail.com"
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "password"
    MAIL_USERNAME = cfg.get("MAIL_USERNAME", "YOU_MAIL@gmail.com")
    MAIL_PASSWORD = cfg.get("MAIL_PASSWORD", "password")
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    FLASK_ADMIN_SWATCH = "cerulean"
    # db_host = "vityah1.mysql.tools"
    # db_user = "vityah1_db"
    # db_passwd = "8QhVlu7R"
    # db_db = "vityah1_db"
    secret_key = "sdfasdfadsfaafduhsdmfjkadshfmasdf53562524j35hm43l5j4m35j43m5l43j5m43l54m5lj43m5l4j35l435h42l5h43l"
    # SQLALCHEMY_DATABASE_URI = f"""mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_db}"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secret_key
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = cfg["secret_key"]


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        # os.environ.get("DEVELOPMENT_DATABASE_URI")
        # or "mysql+pymysql://root:pass@localhost/flask_app_db"
        cfg.get(
            "DEVELOPMENT_DATABASE_URI",
            "mysql+pymysql://vityah1_db:8QhVlu7R@vityah1.mysql.tools/vityah1_db",
        )
    )


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = cfg.get(
        "TESTING_DATABASE_URI",
        "mysql+pymysql://vityah1_db:8QhVlu7R@vityah1.mysql.tools/vityah1_db",
    )


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = cfg.get(
        "PRODUCTION_DATABASE_URI",
        "mysql+pymysql://vityah1_db:8QhVlu7R@vityah1.mysql.tools/vityah1_db",
    )
