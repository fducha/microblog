from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(label=u'Имя пользователя', validators=[DataRequired()])
    password = PasswordField(label=u'Пароль', validators=[DataRequired()])
    remember_me = BooleanField(label=u'Запомнить меня')
    submit = SubmitField(label=u'Войти')


class RegistrationForm(FlaskForm):
    username = StringField(label=u'Имя пользователя', validators=[DataRequired()])
    email = StringField(label=u'E-mail', validators=[DataRequired(), Email()])
    password1 = PasswordField(label=u'Пароль', validators=[DataRequired()])
    password2 = PasswordField(label=u'Повторите пароль', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label=u'Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(u'Используйте другое имя пользователя')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(u'Используйте другой адрес электронной почты ')


class EditProfileForm(FlaskForm):
    username = StringField(label=u'Имя пользователя', validators=[DataRequired()])
    about_me = TextAreaField(label=u'Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField(label=u'Сохранить')
