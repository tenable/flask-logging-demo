from flask import Blueprint, current_app

bp = Blueprint("public", __name__)


@bp.route("/")
def hello_world():
    current_app.logger.info("I'm in a glass case of emotion!")
    current_app.logger.warning("<Lightsaber noises>")
    current_app.logger.error("The lightsabers are _NOT_ helping.")

    return "Hello World!"
