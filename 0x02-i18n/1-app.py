#!/usr/bin/env python3
"""
1-app.py

Basic setup for internationalization using Flask-Babel
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    class Config

    Provides configuration info for flask app instance
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@app.route('/', strict_slashes=False)
def get_template_page() -> str:
    """
    get_template_page() route handler
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=5001)
