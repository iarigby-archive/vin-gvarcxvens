#!/usr/bin/env python

from flask import Flask

app = Flask(__name__ )

import functions as api

@app.route('/')
def hello_world():
    return api.get_main_page()
