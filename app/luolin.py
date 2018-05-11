from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = LoginForm()
    print(form.data)
    if form.validate_on_submit():
        return "sdfsdf"
    return render_template('index.html')


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hjkalsdjflasdf'
    app.config['CSRF_ENABLED'] = True
    app.config['DEBUG'] = True
    app.run()
