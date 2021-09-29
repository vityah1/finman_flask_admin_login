from flask import Blueprint

api_bp = Blueprint("api_bp", __name__)
api_crud_bp = Blueprint("api_crud_bp", __name__)

from . import views, views_crud
