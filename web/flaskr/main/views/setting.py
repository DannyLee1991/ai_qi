from flask import render_template, make_response
from .. import main
from ..form.setting_forms import *
from utils.flash import *


@main.route('/setting')
def setting():
    return setting_response()


@main.route('/setting/<form_id>', methods=['GET', 'POST'])
def setting_for(form_id):
    form = get_form(form_id)
    if form.validate_on_submit():
        type = form.type.data
        db_name = form.db_name.data
        user_name = form.user_name.data
        pass_word = form.pass_word.data
        # 设置tudata的数据库配置
        tu.set_db_config(type,db_name,user_name,pass_word)

        flash_success("设置成功")

    return setting_response(form=form)


setting_form_info = lambda id, name, form: {"id": id, "name": name, "form": form}


def get_form_info_list():
    return [setting_form_info("setting_for_tudata",
                              "数据存储设置",
                              TuDataConfigForm())]


def get_form(id):
    for form_info in get_form_info_list():
        if form_info['id'] == id:
            return form_info['form']


def setting_response(form=None):
    return make_response(render_template('setting.html',
                                         form_info_list=get_form_info_list(),
                                         form=form))
