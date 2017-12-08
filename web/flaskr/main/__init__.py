from flask import Blueprint

main = Blueprint('main', __name__)

from .views import index, setting, getdata, tables, visualization
from .api import query
