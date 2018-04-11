# -*- coding: utf-8 -*-
from app import application
from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    title = 'Привет всем!!!'
    user = {'username': 'fducha Петров'}
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
    return render_template('index.html', title=title, user=user, posts=posts)