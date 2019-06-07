from flask import Flask, current_app, request
from flask_logs import LogSetup
from datetime import datetime as dt
import logging
import os

app = Flask(__name__)

# Logging Setup - This would usually be stuffed into a settings module
# Default output is a Stream (stdout) handler, also try out "watched" and "file"
app.config["LOG_TYPE"] = os.environ.get("LOG_TYPE", "stream")
app.config["LOG_LEVEL"] = os.environ.get("LOG_LEVEL", "INFO")

# File Logging Setup
# app.config['LOG_DIR'] = os.environ.get("LOG_DIR", "./")
# app.config['APP_LOG_NAME'] = os.environ.get("APP_LOG_NAME", "app.log")
# app.config['WWW_LOG_NAME'] = os.environ.get("WWW_LOG_NAME", "www.log")
# app.config['LOG_MAX_BYTES'] = os.environ.get("LOG_MAX_BYTES", 100_000_000)  # 100MB in bytes
# app.config['LOG_COPIES'] = os.environ.get("LOG_COPIES", 5)

logs = LogSetup()
logs.init_app(app)


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


@app.route("/")
def hello_world():
    current_app.logger.info("Hello There")
    current_app.logger.error("<Lightsaber noises>")
    current_app.logger.warning("General Kenobi")
    return "Hello World!"


if __name__ == "__main__":
    app.run()
