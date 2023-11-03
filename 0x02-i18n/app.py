#!/usr/bin/env python3
"""
1-app.py

Basic setup for internationalization using Flask-Babel
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Optional, Mapping, Union
from pytz import timezone, UnknownTimeZoneError


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
    supported_locales = app.config['LANGUAGES']
    default_locale = app.config['BABEL_DEFAULT_LOCALE']
    if 'locale' in request.args:
        locale = request.args.get('locale')
    elif g.user:
        locale = g.user.get('locale')
    else:
        locale = request.accept_languages.best_match(supported_locales)

    if locale and locale in supported_locales:
        return locale
    else:
        return default_locale
    

@babel.timezoneselector
def get_timezone() -> str:
    """
    get_timezone() babel handler function
    """
    default_time_zone = app.config['BABEL_DEFAULT_TIMEZONE']
    if 'timezone' in request.args:
        time_zone_str = request.args.get('timezone')
    elif g.user:
        time_zone_str = g.user.get('timezone')
    else:
        time_zone_str = default_time_zone

    try:
        timezone(time_zone_str)
    except UnknownTimeZoneError:
        return default_time_zone
    return time_zone_str


@app.route('/', strict_slashes=False)
def get_template_page() -> str:
    """
    get_template_page() route handler
    """
    current_time = format_datetime(datetime.now())
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
