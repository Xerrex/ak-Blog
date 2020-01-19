import os
from app import create_app, cli

app_environment = os.getenv('FLASK_CONFIG') or 'production'
app = create_app(app_environment)

cli.register(app)
