from flask import Blueprint

main = Blueprint('main', __name__)

from .views import index, setting, getdata, tables, visualization
from .views.data_views import trans_d
from .api import query
