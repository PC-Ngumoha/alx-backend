#!/usr/bin/env python3
"""
0-app.py

Basic flask app providing the template for the rest of the project
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_template_page() -> str:
    """
    get_template_page() route handler
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5001)
