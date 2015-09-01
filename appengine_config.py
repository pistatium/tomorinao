"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""
import os
import sys
from google.appengine.ext import vendor

ROOTPATH = os.path.dirname(__file__)
SRCPATH = os.path.join(ROOTPATH, 'src')
sys.path.append(SRCPATH)

vendor.add('libraries')
