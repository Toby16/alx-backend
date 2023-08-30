#!/usr/bin/env python3
"""
Get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    class to configure available languages in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
config = app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale for a web page
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    view function to render '2-index.html'
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
