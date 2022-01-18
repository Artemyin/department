import os
from flask import Flask

def get_env():
    return os.environ.get("prod", "dev")

def create_app():
    """[summary]

    Returns:
        [type]: [description]
    """
    app = Flask(__name__)
    env = get_env()
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