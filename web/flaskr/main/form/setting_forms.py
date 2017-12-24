from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required
import tudata as tu


class TuDataConfigForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(TuDataConfigForm, self).__init__(*args,
                                               **kwargs)
        self.type.choices = []
        for type in tu.support_db_types:
            self.type.choices.append((type,type))

    type = SelectField('数据库类型')
    db_name = StringField('请输入数据库名称', default='tu', validators=[Required()])
    user_name = StringField('请输入用户名', validators=[Required()])
    pass_word = StringField('密码', validators=[Required()])
    submit = SubmitField('确定')
