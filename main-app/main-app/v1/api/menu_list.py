# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Recipes as Re, Ingredients as In, Menus as Ms, MenuDetails as Me
from ..helpers import authorize

from . import Resource
from .. import schemas


class MenuList(Resource):

    def get(self):
        authorize(g.headers)

        menu = Me.select().order_by(Me.id)
        menu_res = []
        for me in menu:
            menu_s = Ms.select().where(
                Ms.menu_id == me.id)
            r_res = []
            for m in menu_s:
                # print("m-----", flush=True)
                # print(m.recipe_id, flush=True)
                recipe = Re.select().where(Re.id == m.recipe_id)
                # print("recipe-----", flush=True)
                # print(recipe, flush=True)
                for r in recipe:
                    # print("r-----", flush=True)
                    # print(r.name, flush=True)
                    in_res = []
                    ingredients = In.select().where(In.recipe_id == r.id)
                    for i in ingredients:
                        # print("i-----", flush=True)
                        # print(i.name, flush=True)
                        # print("i-----", flush=True)
                        # print(i.name, flush=True)
                        in_res.append({
                            "name": i.name,
                            "image": i.image
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
            menu_res.append({
                "id": me.id,
                "uuid": me.uuid,
                "week": me.week,
                "year": me.year,
                "description": me.description,
                "recipes": r_res
            })

        return menu_res, 200, None
