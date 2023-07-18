import os
from flask import Flask


def get_env():
    """Get enviroment variable.
    Returns:
       enviroment variable: application settings
    """
    return os.environ.get("ENV", "dev")


def create_app():
    """Application Factory.
    Instansing flask app,
    Get settings from settings.py
    Initialising models, serializers, views, rest
    Returns:
       app: application
    """
    app = Flask(__name__)
    env = get_env()
    # logger.info(f"Environment: {env}")
    if env == "prod":
        env_config = os.getenv("APP_SETTINGS", "config.ProductionConfig")
    else:
        env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    from . import models, serializers, views, rest
    models.init_app(app)
    serializers.init_app(app)
    views.init_app(app)
    rest.init_app(app)

    return app


app = create_app()
