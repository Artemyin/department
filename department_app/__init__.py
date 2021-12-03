import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    from . import models, serializers, migrations, views
    models.init_app(app)
    serializers.init_app(app)
    migrations.init_app(app)
    views.init_app(app)

    return app

