# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Ingredients

from . import Resource
from .. import schemas


class IngredientsList(Resource):

    def get(self):
        print(g.headers)
        print(g.args)

        return [], 200, None
