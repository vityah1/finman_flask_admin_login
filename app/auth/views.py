from app import db
from . import auth
from flask import render_template, request, redirect, url_for, flash, make_response
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User
from .forms import LoginForm, SigUpForm
from werkzeug.security import generate_password_hash


@auth.route("/user/<int:user_id>/")
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@auth.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


@auth.route("/signup", methods=["GET"])
def signup():
    form = SigUpForm()
    return render_template("signup.html", form=form)


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash(f"username {username} is exist", "error")
        return redirect(url_for("main.signup"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(
        email=email,
        name=name,
        username=username,
        password_hash=generate_password_hash(password, method="sha256"),
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("main.login"))


@auth.route("/login/", methods=["post", "get"])
def login():
    if current_user.is_authenticated:
        # return redirect(url_for("app.admin"))
        return redirect(url_for("admin.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = (
            db.session.query(User).filter(User.username == form.username.data).first()
        )
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            # return redirect(url_for("app.admin"))
            return redirect(url_for("admin.index"))
        else:
            flash("Invalid username/password", "error")
            return redirect(url_for(".login"))
    return render_template("login.html", form=form)


@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for(".login"))


@auth.route("/cookie/")
def cookie():
    if not request.cookies.get("foo"):
        res = make_response("Setting a cookie")
        res.set_cookie("foo", "bar", max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Value of cookie foo is {}".format(request.cookies.get("foo"))
        )
    return res


@auth.route("/delete-cookie/")
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie("foo", "bar", max_age=0)
    return res
