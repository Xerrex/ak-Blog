import os
from my_core.app import create_app
from my_core.utils.extensions import db
from my_core.models import User, Post, Message, \
        Notification, Task

env_config = os.getenv('FLASK_CONFIG') or 'prod'
app = create_app(env_config)

@app.shell_context_processor
def make_shell_context():
    models = {
        'db': db, 
        'User': User, 
        'Post': Post, 
        'Message': Message,
        'Notification': Notification,
        'Task': Task
    }
    return models

if __name__ == '__main__':
    app.run()