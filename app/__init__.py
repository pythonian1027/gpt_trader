# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:45:46 2023

@author: ricor
"""


# app/__init__.py
from flask import Flask

app = Flask(__name__)

from app import routes
