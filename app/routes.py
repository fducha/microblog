# -*- coding: utf-8 -*-
from app import application, db
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.forms import RegistrationForm, EditProfileForm
from datetime import datetime


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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form, title='Sing In')


@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'Поздравляем, пользователь {} <{}> зарегистрирован!!'.format(user.username, user.email))
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title=u'Регистрация')


@application.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'test post #1'},
        {'author': user, 'body': 'test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@application.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=u'Редактирование профиля', form=form)


@application.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
