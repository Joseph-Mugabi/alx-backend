#!/usr/bin/env python3

"""
Module instantiates babel object
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configures language """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


strict_slashes = False
@app.route("/")
def welcome_HBN():
    """renders 2-index.html"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """get best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
