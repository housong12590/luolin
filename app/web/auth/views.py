from flask_classy import FlaskView
from flask import render_template, request, redirect, url_for
from .forms import LoginForm, RegisterForm
from app.models import User
from app import db


class AuthView(FlaskView):
    route_base = 'auth'

    def login(self):
        print(url_for('web.AuthView:login'))
        form = LoginForm()
        if request.method == 'POST' and form.validate_on_submit():
            # user = db.session.query(User).filter(User.username == form.username).first()
            return 'Main.index'
        return render_template('auth/login.html', form=form)

    def __register(self):
        form = RegisterForm()
        if request.method == 'POST' and form.validate_on_submit():
            user = User(1, '')
            db.session.add(user)
            db.session.commit()
            return 'Main.index'
        return render_template('auth/register.html', form=form)
