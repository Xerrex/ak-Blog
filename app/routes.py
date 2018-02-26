from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user

from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex Kagai'}
    posts = [
        {
            'author': {'username': 'Nick'},
            'body': 'My Dear Futurre wife'
        },
        {
            'author': {'username': 'Gitau'},
            'body': 'Kenya my Country'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=login_form)