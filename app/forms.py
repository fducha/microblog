from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(label=u'Имя пользователя', validators=[DataRequired()])
    password = PasswordField(label=u'Пароль', validators=[DataRequired()])
    remember_me = BooleanField(label=u'Запомнить меня')
    submit = SubmitField(label=u'Войти')