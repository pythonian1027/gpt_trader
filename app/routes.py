# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:46:35 2023

@author: ricor
"""

# app/routes.py
from app import app

@app.route('/')
def index():
    return 'Hello, World!'

