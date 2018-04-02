# -*- coding: utf-8 -*-
"""Initialisation file for lib module."""
import os

import cherrypy

# Absolute path to the "mlserver" directory, which is considered to be the
# main application directory within this project.
APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def updateHTTPConfig():
    """Read the http config files and update CherryPy config.

    This must be done here rather than app.py, to ensure the settings are
    applied to other scripts which use cherrypy such as for logging.
    """
    confDir = os.path.join(APP_DIR, 'etc')

    for httpFile in ('http.conf', 'http.local.conf'):
        cherrypy.config.update(os.path.join(confDir, httpFile))


def updateLogConfig():
    """Read the log configuration files and add values to CherryPy config.

    This is necessary even when not running the main app, so that any messages
    logged in other modules are logged to the correct location.
    """
    for filename in ['log.conf', 'log.local.conf']:
        logConf = os.path.join(APP_DIR, 'etc', filename)

        # Skip a file which does not exist, to avoid cherrypy raising
        # an exception.
        if os.access(logConf, os.R_OK):
            cherrypy.config.update(logConf)


updateHTTPConfig()

updateLogConfig()
logger = cherrypy.log