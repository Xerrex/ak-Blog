from flask import redirect, url_for, flash, request, render_template
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask_babel import _

from app import db
from app.models import User

from . import auth_bp
from .forms import LoginForm, RegistrationForm, ResetPasswordForm, \
    ResetPasswordRequestForm
from .email import send_password_reset_email


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        login_user(user, remember=login_form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.index')
        return redirect(next_page)

    return render_template('auth/login.html', title=_('Sign In'), form=login_form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user = User(username=reg_form.username.data, email=reg_form.email.data)
        user.set_password(reg_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        return redirect(url_for('auth.login'))
    return render_template('register.html', title=_('Register'), form=reg_form)


@auth_bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    reset_password_request_form = ResetPasswordRequestForm()
    if reset_password_request_form.validate_on_submit():
        user = User.query.filter_by(email=reset_password_request_form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('auth.login'))
    return render_template('reset_password_request.html', title=_('Reset Password'),
                           form=reset_password_request_form)


@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('home.index'))
    reset_password_form = ResetPasswordForm()
    if reset_password_form.validate_on_submit():
        user.set_password(reset_password_form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', form=reset_password_form)

