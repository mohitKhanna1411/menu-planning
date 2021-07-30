# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Recipes as Re
from ..helpers import authorize
import uuid
from . import Resource
from .. import schemas


class Recipe(Resource):

    def get(self):
        authorize(g.headers)
        data = request.get_json()

        recipe = Re.select().where(Re.uuid ==
                                   data.get('uuid')).dicts().get()
        if not recipe:
            return {"message": "Ingredient not found"}, 404, None
        return recipe, 200, None

    def post(self):
        authorize(g.headers)
        data = request.get_json()

        print(data, flush=True)
        Re.create(
            uuid=str(uuid.uuid4()),
            name=data.get('name'),
            image=data.get('image'),
            steps=data.get('steps'),
            classification=data.get('classification'),
            nutirtional_information=data.get('nutirtional_information'),
        )
        return {"message": "Success"}, 200, None

    def put(self):
        authorize(g.headers)
        data = request.get_json()

        recipe = Re.select().where(
            Re.uuid == data.get('uuid')).get()
        if not recipe:
            return {"message": "Ingredient not found"}, 404, None

        recipe.name = 'new name'
        recipe.image = 'new image'
        recipe.save()  # Will do the SQL update query.
        # print(g.json)
        # print(g.headers)
        # print(g.args)

        return {"message": "Success"}, 200, None

    def delete(self):
        authorize(g.headers)
        data = request.get_json()

        ingredient = Re.get(Re.uuid == data.get('uuid'))
        if not ingredient:
            return {"message": "Ingredient not found"}, 404, None
        ingredient.delete_instance()
        # print(g.headers)
        # print(g.args)

        return {}, 200, None
