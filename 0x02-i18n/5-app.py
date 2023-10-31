#!/usr/bin/env python3
"""
1-app.py

Basic setup for internationalization using Flask-Babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Mapping, Union


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Mapping, None]:
    """
    get_user() helper function
    """
    if 'login_as' in request.args:
        id = int(request.args.get('login_as'))
        return users.get(id, None)


@app.before_request
def before_request() -> None:
    """
    before_request() function, called before all other functions
    """
    g.user = get_user()


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5001)
