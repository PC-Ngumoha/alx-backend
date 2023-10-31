#!/usr/bin/env python3
"""
1-app.py

Basic setup for internationalization using Flask-Babel
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """
    get_locale() babel handler function
    """
    locale = request.args['locale'] if 'locale' in request.args else None
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def get_template_page() -> str:
    """
    get_template_page() route handler
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port=5001)
