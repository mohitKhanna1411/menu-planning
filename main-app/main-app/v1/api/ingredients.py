# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Ingredients as In
from ..helpers import authorize
import uuid

from . import Resource
from .. import schemas


class Ingredients(Resource):

    def get(self):
        authorize(g.headers)
        data = request.get_json()

        ingredient = In.select().where(In.uuid ==
                                       data.get('uuid')).dicts().get()
        if not ingredient:
            return {"message": "Ingredient not found"}, 404, None
        return ingredient, 200, None

    def post(self):

        authorize(g.headers)
        data = request.get_json()

        print(data, flush=True)
        In.create(
            uuid=str(uuid.uuid4()),
            name=data.get('name'),
            image=data.get('image')
        )
        return {"message": "Success"}, 200, None

    def put(self):
        authorize(g.headers)
        data = request.get_json()

        ingredient = In.select().where(
            In.uuid == data.get('uuid')).get()
        if not ingredient:
            return {"message": "Ingredient not found"}, 404, None

        ingredient.name = 'new name'
        ingredient.image = 'new image'
        ingredient.save()  # Will do the SQL update query.
        # print(g.json)
        # print(g.headers)
        # print(g.args)

        return {"message": "Success"}, 200, None

    def delete(self):
        authorize(g.headers)
        data = request.get_json()

        ingredient = In.get(In.uuid == data.get('uuid'))
        if not ingredient:
            return {"message": "Ingredient not found"}, 404, None
        ingredient.delete_instance()
        # print(g.headers)
        # print(g.args)

        return {}, 200, None
