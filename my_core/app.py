from flask import Flask
from flask_babel import lazy_gettext as _l

from config import env_configs
from .utils.extensions import ext_app_init
from .utils.app_logging import app_logger


def create_app(env):
    """Create Flask application 

    Args:
        env_config (String): enviroment settings (prod, dev, testing)

    Returns:
        Flask: flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(env_configs[env])
    
    ext_app_init(app) # initializie extensions

    from .error import error_bp
    app.register_blueprint(error_bp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .home import home_bp
    app.register_blueprint(home_bp)

    app_logger(app) # Logging operations

    return app
