import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ghb3DwdawdaWefefHTGRhGSkjfGehkjsSGe6S26262bjghf11'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'app.db')