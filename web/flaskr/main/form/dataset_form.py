from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label
from wtforms.validators import Required, Length, Email, Regexp, NumberRange


class CreateTransDDataSetForm(FlaskForm):
    def __init__(self, start_date_def, end_date_def, *args, **kwargs):
        super(CreateTransDDataSetForm, self).__init__(*args, **kwargs)
        self.start_date.data = start_date_def
        self.end_date.data = end_date_def

    name = StringField('请输入数据集名称', validators=[Required()])
    start_date = StringField('起始日期', id='ip_date_start')
    end_date = StringField('结束日期', id='ip_date_end')
    date_offset = StringField('时间差', validators=[Required(),
                                                 Regexp('^[0-9]*$', 0,
                                                        '请输入数值')])
    submit = SubmitField('生成')


class ContinueBuildForm(FlaskForm):
    submit = SubmitField('继续构建数据集')
