from flask import Flask

from .routes.planet import planets_bp


def create_app(test_config=None):
    app = Flask(__name__)
    # Register Blueprints
    app.register_blueprint(planets_bp)

    return app
