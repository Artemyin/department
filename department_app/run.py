import os
from flask import Flask



def create_app():
    """[summary]

    Returns:
        [type]: [description]
    """
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    from . import models, serializers, views, rest
    models.init_app(app)
    serializers.init_app(app)
    views.init_app(app)
    rest.init_app(app)

    return app

app = create_app()

app.run()