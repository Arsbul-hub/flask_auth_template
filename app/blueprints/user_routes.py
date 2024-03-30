from urllib.parse import urlsplit

from flask import redirect, render_template, request, url_for, flash
from flask_login import logout_user, login_required, login_user, current_user

from app import db, login_blueprint
from app.forms import LoginForm, RegistrationForm
from app.models import User


@login_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
            return next_page
        return redirect("/user_panel")
    return render_template('forms/login.html', user=current_user, title='Sign In', form=form)


@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.username.data
        user.set_password(form.password.data)
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()
        # login_user(user, remember=form.css.remember_me.data)
        flash('Congratulations, you are now a registered admin!')
        login_user(user, True)
        return redirect(url_for('index'))
    return render_template('forms/register.html', user=current_user, title='Register', form=form)


@login_blueprint.route("/user_panel", methods=['GET', 'POST'])
@login_required
def user_panel():
    return render_template("user_panel.html", user=current_user)
