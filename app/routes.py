from flask import render_template

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

@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Sign In', form=login_form)