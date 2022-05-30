from flask import render_template, request, redirect, url_for

from . import web

__author__ = 'zx.y'

from ..forms.auth import RegisterForm, LoginForm
from ..models.base import db
from ..models.user import User


@web.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit()
            redirect(url_for('web.login'))
    except:
        db.session.rollback()
    return render_template('auth/register.html',form = form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('auth/login.html',form = form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
