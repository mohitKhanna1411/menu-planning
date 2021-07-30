# -*- coding: utf-8 -*-
from __future__ import absolute_import
from v1.models import create_db

from flask import Flask

import v1

db_name = 'hellofresh.db'


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app


if __name__ == '__main__':
    create_db(db_name)
    create_app().run(debug=True, host='0.0.0.0', port=8090)
