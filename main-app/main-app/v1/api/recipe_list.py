# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Ingredients as In
from ..models import Recipes as Re
from ..helpers import authorize

from . import Resource
from .. import schemas


class RecipeList(Resource):

    def get(self):
        print(g.headers)
        authorize(g.headers)

        recepie = Re.select().order_by(Re.id)
        r_res = []
        for r in recepie:
            in_res = []
            print("r-----", flush=True)
            print(r.id, flush=True)
            ingredients = In.select().where(In.recipe_id == r.id)
            for i in ingredients:
                print("i-----", flush=True)
                print(i.name, flush=True)
                in_res.append({
                    "name": i.name,
                    "image":i.image
                })
            r_res.append({
                'id': r.id,
                'uuid': r.uuid,
                'name': r.name,
                'created_at': r.created_at,
                'classification': r.classification,
                'image': r.image,
                'nutirtional_information': r.nutirtional_information,
                'ingredients': in_res,
            })

        # print(recepie)

        return r_res, 200, None
