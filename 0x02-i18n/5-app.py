#!/usr/bin/env python3
"""
Mock logging in
"""

from flask import (
        Flask,
        render_template,
        request,
        g)
from flask_babel import Babel
from typing import Union, Dict


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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user based on a user id
    """
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale for a web page
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
     return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    view function to render '4-index.html'
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
