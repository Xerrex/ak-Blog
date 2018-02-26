from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm

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
    login_form = LoginForm()

    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=login_form)