from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex Kagai'}
    return render_template('index.html', title='Home', user=user)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name