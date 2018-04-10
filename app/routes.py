# -*- coding: utf-8 -*-
from app import application


@application.route('/')
@application.route('/index')
def index():
    return 'Привет всем!!'