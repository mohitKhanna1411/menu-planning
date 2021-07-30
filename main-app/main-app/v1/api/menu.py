# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Menu(Resource):

    def get(self):
        print(g.headers)
        print(g.args)

        return {}, 200, None

    def post(self):
        print(g.json)
        print(g.headers)

        return {}, 200, None

    def put(self):
        print(g.json)
        print(g.headers)
        print(g.args)

        return {}, 200, None

    def delete(self):
        print(g.headers)
        print(g.args)

        return {}, 200, None