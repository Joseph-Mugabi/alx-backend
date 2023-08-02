#!/usr/bin/env python3

"""Module implements flask app"""

from flask import Flask, render_template


app = Flask(__name__)


strict_slashes = False
@app.route("/")
def welcome_HBN():
    """renders 0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
