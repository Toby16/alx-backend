#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    view function to render 'index.html'
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')