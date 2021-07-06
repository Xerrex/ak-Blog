from flask import request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

from elasticsearch import Elasticsearch
from redis import Redis
import rq

from .cli_translate import cli_init_app


app = None
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
migrate = Migrate()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def ext_app_init(app):
    """Initialize apps with extensions

    Args:
        app (Flask): Flask app instance
    """
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    cli_init_app(app) #translate commands

    elastic_cfg = app.config['ELASTICSEARCH_URL']
    app.elasticsearch = Elasticsearch(elastic_cfg) if elastic_cfg else None

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('AK-BLOG-tasks', connection=app.redis)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])