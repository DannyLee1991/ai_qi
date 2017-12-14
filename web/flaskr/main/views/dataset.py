from flask import render_template, make_response
from .. import main
import dataset as ds


@main.route('/dataset_manage')
def dataset_manage():
    info_list = ds.get_all_dataset_info_list()
    resp = make_response(render_template('dataset.html', info_list=info_list))
    return resp


@main.route('/dataset_manage/add')
def dataset_add():
    creater_list = ds.DATASET_CREATER_LIST
    return make_response(render_template('dataset_add.html', creater_list=creater_list))


@main.route('/dataset_manage/add/<type>')
def dataset_add_type(type):
    creater_list = ds.DATASET_CREATER_LIST

    if type == ds.TYPE_TRANS_D:
        return make_response(render_template('dataset_creater/trans_d.html', creater_list=creater_list))
    return make_response(render_template('dataset_add.html'))
