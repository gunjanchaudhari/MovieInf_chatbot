# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v1

from flask_cors import CORS 

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app, resources={r"/*": {"origins": "*"}}) 
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
