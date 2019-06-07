import logging
from datetime import datetime as dt

from flask import Flask, request

from . import public
from .extensions import logs


def create_app(config_object="log_demo_factory.settings"):
    """Main app factory, runs all the other sections"""
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    return app


def register_extensions(app):
    logs.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(public.views.bp)
    return None
