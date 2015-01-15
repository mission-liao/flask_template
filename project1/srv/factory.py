from __future__ import absolute_import
from flask import Flask
import logging
from ..defs import APP_DEFAULT_PACKAGE_NAME, APP_CONFIG_NAME, APP_DEFAULT_CONFIG_NAME


def create_app(package_name=None, settings_override=None):
    package_name = package_name or APP_DEFAULT_PACKAGE_NAME
    app = Flask(package_name, instance_relative_config=True)

    # try to import global config
    if package_name != APP_DEFAULT_PACKAGE_NAME:
        try:
            __import__(APP_DEFAULT_CONFIG_NAME)
            app.config.from_object(APP_DEFAULT_CONFIG_NAME)
        except ImportError:
            pass

    # try to import per-package config
    try:
        config_path = package_name + '.' + APP_CONFIG_NAME
        
        __import__(config_path)
        app.config.from_object(config_path)
    except ImportError:
        pass

    # override by settings provided by caller.
    if settings_override:
        app.config.from_pyfile(settings_override)

    return app


def create_rest_app(app=None, package_name=None):
    app = app or create_app(package_name)

    # init logging
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

    return app

