from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db_host = "vityah1.mysql.tools"
db_user = "vityah1_db"
db_passwd = "8QhVlu7R"
db_db = "vityah1_db"
secret_key = "sdfasdfadsfaafduhsdmfjkadshfmasdf53562524j35hm43l5j4m35j43m5l43j5m43l54m5lj43m5l4j35l435h42l5h43l"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"""mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_db}"""
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username
