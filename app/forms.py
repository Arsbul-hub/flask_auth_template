from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms.fields import *
from wtforms.validators import DataRequired, Email

from app.models import User
from app.validators import *


class LoginForm(FlaskForm):
    _name = "Вход"
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()

        if not user or not user.check_password(password.data):
            raise ValidationError('Неверная электронная почта или неверен пароль.')


class RegistrationForm(FlaskForm):
    _name = "Регистрация"
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField("Электронная почта", validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повтор пароля', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя занято')

    def validate_password2(self, password):
        if password.data != self.password.data:
            raise ValidationError('Пароли не совпадают')
