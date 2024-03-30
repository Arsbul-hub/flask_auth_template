from flask import render_template, redirect
from flask_login import current_user

from app import app, login
from app.forms import *


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("user_panel")
    return redirect("login")
