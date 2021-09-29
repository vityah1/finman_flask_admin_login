from app import db
from . import main
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    make_response,
    session,
    current_app,
)
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User, Feedback
from app.utils import send_mail
from .forms import ContactForm, LoginForm, SigUpForm
from werkzeug.security import generate_password_hash


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/user/<int:user_id>/")
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


# @main.route("/books/<genre>/")
# def books(genre):
#     return "All Books in {} category".format(genre)
@main.route("/signup", methods=["GET"])
def signup():
    form = SigUpForm()
    return render_template("signup.html", form=form)


@main.route("/signup", methods=["POST"])
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


@main.route("/login/", methods=["post", "get"])
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


@main.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for(".login"))


@main.route("/contact/", methods=["get", "post"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # логика БД здесь
        feedback = Feedback(name=name, email=email, message=message)
        db.session.add(feedback)
        db.session.commit()

        send_mail(
            "New Feedback",
            current_app.config["MAIL_DEFAULT_SENDER"],
            "mail/feedback.html",
            name=name,
            email=email,
        )

        flash("Message Received", "success")
        return redirect(url_for(".contact"))

    return render_template("contact.html", form=form)


@main.route("/cookie/")
def cookie():
    if not request.cookies.get("foo"):
        res = make_response("Setting a cookie")
        res.set_cookie("foo", "bar", max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Value of cookie foo is {}".format(request.cookies.get("foo"))
        )
    return res


@main.route("/delete-cookie/")
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie("foo", "bar", max_age=0)
    return res


# @main.route("/article", methods=["POST", "GET"])
# def article():
#     if request.method == "POST":
#         res = make_response("")
#         res.set_cookie("font", request.form.get("font"), 60 * 60 * 24 * 15)
#         res.headers["location"] = url_for(".article")
#         return res, 302

#     return render_template("article.html")


# @main.route("/visits-counter/")
# def visits():
#     if "visits" in session:
#         session["visits"] = session.get("visits") + 1
#     else:
#         session["visits"] = 1
#     return "Total visits: {}".format(session.get("visits"))


# @main.route("/delete-visits/")
# def delete_visits():
#     session.pop("visits", None)  # удаление посещений
#     return "Visits deleted"


# @main.route("/session/")
# def updating_session():
#     res = str(session.items())

#     cart_item = {"pineapples": "10", "apples": "20", "mangoes": "30"}
#     if "cart_item" in session:
#         session["cart_item"]["pineapples"] = "100"
#         session.modified = True
#     else:
#         session["cart_item"] = cart_item

#     return res


# @main.route('/admin/')
# @login_required
# def admin():
#     return render_template('admin.html')
