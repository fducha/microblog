# -*- coding: utf-8 -*-
from app import application, db
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, url_for, redirect, request
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm


@application.route('/')
@application.route('/index')
@login_required
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


@application.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(u'Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@application.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash(u'Поздравляем!! Вы зарегистрированы как {}'.format(user.username))
        return redirect(url_for('login'))
    return render_template("register.html", title=u'Регистрация', form=form)


@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
