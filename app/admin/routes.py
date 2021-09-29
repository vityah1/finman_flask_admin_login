from flask_admin.contrib.sqla import ModelView

# from flask_admin import expose
from app import db, admin
from app.models import User, myBudj, myBudj_sub_cat, myBudj_spr_cat
from flask_login.utils import current_user
from flask_admin.menu import MenuLink
from flask import redirect, url_for, request


class MyView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_accessible(self):
        # return current_user.is_authenticated and current_user.is_admin
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("main.login", next=request.url))


admin.add_view(MyView(User, db.session))
admin.add_view(MyView(myBudj, db.session))
admin.add_view(ModelView(myBudj_spr_cat, db.session))
admin.add_view(ModelView(myBudj_sub_cat, db.session))
admin.add_link(MenuLink(name="Main", category="", url="/"))
admin.add_link(MenuLink(name="Login", category="", url="/login/"))
admin.add_link(MenuLink(name="Logout", category="", url="/logout/"))
