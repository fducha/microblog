# -*- coding: utf-8 -*-
from app import application
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import User


@application.route('/')
@application.route('/index')
def index():
    title = 'Привет всем!!!'
    posts = [
        {
            'author': {'username': 'user One'},
            'body': 'This is the first post'
        },
        {
            'author': {'username': 'user Two'},
            'body': 'This is the second post'
        },
        {
            'author': {'username': 'user Three'},
            'body': 'This is the third post'
        },
        {
            'author': {'username': 'user Four'},
            'body': 'This is the fourth post'
        },
        {
            'author': {'username': 'user Five'},
            'body': 'This is the fivth post'
        },
        {
            'author': {'username': 'user Six'},
            'body': 'This is the Sixth post'
        }
    ]
    return render_template('index.html', title=title, posts=posts)


@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(u'Неправильное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user=user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Sing In')


@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
