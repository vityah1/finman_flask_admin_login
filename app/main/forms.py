from flask_wtf import FlaskForm
from wtforms import Form, ValidationError
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email

style = {"class": "input is-large"}
style_btn = {"class": "button is-block is-info is-large is-fullwidth"}


class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("Username", render_kw=style, validators=[DataRequired()])
    password = PasswordField("Password", render_kw=style, validators=[DataRequired()])
    remember = BooleanField("Remember Me", render_kw={"class": "checkbox"})
    submit = SubmitField(render_kw=style_btn)


class SigUpForm(FlaskForm):

    username = StringField("Username", render_kw=style, validators=[DataRequired()])
    name = StringField("Name", render_kw=style, validators=[DataRequired()])
    email = StringField("E-mail", render_kw=style, validators=[DataRequired()])
    password = PasswordField("Password", render_kw=style, validators=[DataRequired()])
    submit = SubmitField(render_kw=style_btn)
