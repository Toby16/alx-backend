#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    class to configure available languages in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    app = Flask(__name__)
    babel = Babel(app)

    @app.route("/", strict_slashes=False)
    def index() -> str:
        """
        view function to render '1-index.html'
        """
        return render_template("1-index.html")


if __name__ == "__main__":
    Config.app.run(debug=True, port=5000, host="0.0.0.0")
