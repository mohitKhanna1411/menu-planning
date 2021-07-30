# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify
from ..models import Recipes as Re
from ..models import Ingredients as In
from ..helpers import authorize
import uuid
from . import Resource
from .. import schemas
from playhouse.shortcuts import model_to_dict


class Recipe(Resource):

    def get(self):
        authorize(g.headers)
        uuid = g.args.get('uuid')
        print(uuid, flush=True)
        try:
            recipe = Re.select().where(Re.uuid == uuid).dicts().get()
        except Re.DoesNotExist:
            return {"message": "Recipe not found"}, 404, None
        try:
            ingredients = In.select().where(
                In.recipe_id == recipe['id']).dicts().get()
        except In.DoesNotExist:
            ingredients = []
        return {
            'id': recipe['id'],
            'uuid': recipe['uuid'],
            'name': recipe['name'],
            'created_at': recipe['created_at'],
            'classification': recipe['classification'],
            'image': recipe['image'],
            'nutirtional_information': recipe['nutirtional_information'],
            'ingredients': ingredients,
        }, 200, None

    def post(self):
        authorize(g.headers)
        data = request.get_json()

        print(data, flush=True)
        uniquie_uuid = str(uuid.uuid4())
        Re.create(
            uuid=uniquie_uuid,
            name=data.get('name'),
            image=data.get('image'),
            steps=data.get('steps'),
            classification=data.get('classification'),
            nutirtional_information=data.get('nutirtional_information'),
        )
        recipe = Re.select().where(Re.uuid == uniquie_uuid).dicts().get()
        print(type(recipe))
        return {'id': recipe['id'],
                'uuid': recipe['uuid'],
                'name': recipe['name'],
                'image': recipe['image'],
                'classification': recipe['classification'],
                'nutirtional_information': recipe['nutirtional_information']
                }, 200, None

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
