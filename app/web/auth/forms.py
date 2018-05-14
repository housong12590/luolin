from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Regexp
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    username = StringField(
        label='手机号',
        validators=[
            DataRequired(message='手机号不能为空'),
            Regexp(regex=r'1[\d]{10}', message='手机号格式不正确')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='请输入6~18由数字和字母组成的密码'),
            Regexp(regex=r'.+', message='请输入6~18由数字和字母组成的密码')
        ]
    )

    submit = SubmitField('提交')


class RegisterForm(FlaskForm):
    username = None
    password = None
