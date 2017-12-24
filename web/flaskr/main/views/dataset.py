from flask import render_template, make_response, redirect, url_for
from .. import main
import dataset as ds
from ..form.dataset_form import CreateTransDDataSetForm,ContinueBuildForm
from utils.flash import *
from utils.strutils import perYearStr, todayStr


@main.route('/dataset_manage')
def dataset_manage():
    info_list = ds.get_all_dataset_info_list()
    resp = make_response(render_template('dataset/dataset.html', info_list=info_list))
    return resp


@main.route('/dataset/<type>/<name>',methods=['GET', 'POST'])
def dataset_details(type, name):
    dataset = ds.get_dataset(type, name)
    form = ContinueBuildForm()
    if form.validate_on_submit():
        # 继续构建数据集
        dataset.feed_all()

    return make_response(render_template('dataset/dataset_details.html',
                                         dataset=dataset,
                                         form=form))


@main.route('/dataset-del/<type>/<name>')
def dataset_del(type, name):
    ds.remove_dataset(type, name)
    flash_success("数据集【%s】删除成功" % name)
    return redirect(url_for('main.dataset_manage'))


@main.route('/dataset_manage/add')
def dataset_add():
    return make_response(render_template('dataset/dataset_add.html', creater_list=creater_list()))


@main.route('/dataset_manage/add/<type>', methods=['GET', 'POST'])
def dataset_add_type(type):
    if type == ds.TO_TRANS_D['type']:
        form = CreateTransDDataSetForm(perYearStr(), todayStr())

        if form.validate_on_submit():
            name = form.name.data
            start_date = form.start_date.data
            end_date = form.end_date.data
            date_offset = form.date_offset.data
            if start_date < end_date:
                type = ds.TO_TRANS_D['type']
                dataset = ds.get_dataset(type, name)
                if dataset:
                    flash_danger("类型为【%s】的数据集【%s】已存在，请尝试换一个名字，或删除重名数据集" % (ds.TO_TRANS_D['name'], name))
                else:
                    dataset = ds.gen_trans_d_dataset(name, start_date, end_date, int(date_offset))
                    dataset.feed_all()

                    flash_success("数据集【%s】创建成功" % name)
                return redirect(url_for('main.dataset_manage'))
            else:
                flash_warning("起始日期需小于截止日期")

        return make_response(render_template('dataset/creater/trans_d.html',
                                             creater_list=creater_list(),
                                             form=form))
    return make_response(render_template('dataset/dataset_add.html'))


def creater_list():
    return ds.DATASET_TYPE_OBJ_LIST
