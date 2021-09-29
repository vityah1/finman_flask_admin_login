from app import db, login_manager
from datetime import datetime
from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    current_user,
    logout_user,
)
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class Feedback(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255))
#     last_name = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     confirmed_at = db.Column(db.DateTime())
#     # roles = db.relationship('Role', secondary=roles_users,
#     #                         backref=db.backref('users', lazy='dynamic'))

#     def __str__(self):
#         return self.email

#     def __repr__(self):
#         return "<{}:{}>".format(self.id, self.username)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)


class myBudj(db.Model, UserMixin):
    __tablename__ = "myBudj"
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(99))
    sub_cat = db.Column(db.String(99))
    mydesc = db.Column(db.String(150))
    suma = db.Column(db.Integer)
    currencyCode = db.Column(db.Integer)
    mcc = db.Column(db.Integer)
    rdate = db.Column(db.DateTime())
    type_payment = db.Column(db.String(99))
    id_bank = db.Column(db.String(99))
    owner = db.Column(db.String(99))
    source = db.Column(db.String(99))
    tmp = db.Column(db.String(99))
    deleted = db.Column(db.Integer)
    d_mod_row = db.Column(db.DateTime())
    # roles = db.relationship('Role', secondary=roles_users,
    #                         backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.id


class myBudj_spr_cat(
    db.Model,
):
    __tablename__ = "myBudj_spr_cat"
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(99))
    name = db.Column(db.String(99))
    sub_cat = db.Column(db.String(49))
    ord = db.Column(db.Integer)
    pok = db.Column(db.Integer)
    # roles = db.relationship('Role', secondary=roles_users,
    #                         backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.id


class myBudj_sub_cat(
    db.Model,
):
    __tablename__ = "myBudj_sub_cat"
    id = db.Column(db.Integer, primary_key=True)
    id_cat = db.Column(db.Integer)
    sub_cat = db.Column(db.String(49))
    name = db.Column(db.String(99))
    ord = db.Column(db.Integer)
    # roles = db.relationship('Role', secondary=roles_users,
    #                         backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.id
