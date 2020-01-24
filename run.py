import os
from app import create_app, cli, db
from app.models import User, Post, Message, Notification

app_environment = os.getenv('FLASK_CONFIG') or 'production'
app = create_app(app_environment)

cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}