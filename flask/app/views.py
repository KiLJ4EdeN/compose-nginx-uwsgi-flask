#!/usr/bin/env python3
from app import app


@app.route('/')
def index():
    return "Greetings from Flask!"


@app.route('/about')
def about():
    return "This is a simple flask web app!"
