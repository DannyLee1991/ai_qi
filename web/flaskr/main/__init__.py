from flask import Blueprint

main = Blueprint('main', __name__)

from .views import index, setting, getdata, tables, visualization
from .views.data_views import view_trans_d, view_overall_bar
from .api import query
