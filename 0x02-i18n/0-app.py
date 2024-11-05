#!/usr/bin/env python3
"""handling request to root URL /"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home() -> str:
    """ return template 0-index.html """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
