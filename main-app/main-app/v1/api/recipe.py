# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify
from ..models import Recipes as Re, Ingredients as In
from ..helpers import authorize
import uuid
from . import Resource
from .. import schemas


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
                In.recipe_id == recipe['id'])
        except In.DoesNotExist:
            ingredients = []
        in_res = []
        for i in ingredients:
            in_res.append({
                "name": i.name,
                "image": i.image
            })
        return {
            'id': recipe['id'],
            'uuid': recipe['uuid'],
            'name': recipe['name'],
            'created_at': recipe['created_at'],
            'classification': recipe['classification'],
            'image': recipe['image'],
            'nutirtional_information': recipe['nutirtional_information'],
            'ingredients': in_res,
        }, 200, None

    def post(self):
        authorize(g.headers)
        data = request.get_json()

        # print(data, flush=True)
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

        for i in data.get('ingredients'):
            In.create(
                recipe_id=recipe['id'],
                uuid=str(uuid.uuid4()),
                name=i['name'],
                image=i['image']
            )
        print(recipe, flush=True)
        return {'id': recipe['id'],
                'uuid': recipe['uuid'],
                'name': recipe['name'],
                'image': recipe['image'],
                'classification': recipe['classification'],
                'nutirtional_information': recipe['nutirtional_information'],
                'ingredients': data.get('ingredients')
                }, 201, None

    def put(self):
        authorize(g.headers)
        data = request.get_json()
        try:
            recipe = Re.select().where(
                Re.uuid == g.args.get('uuid')).get()
        except Re.DoesNotExist:
            return {"message": "Recipe not found"}, 404, None
        # print(data, flush=True)
        recipe.name = data.get('name')
        recipe.image = data.get('image')
        recipe.classification = data.get('classification')
        recipe.nutirtional_information = data.get('nutirtional_information')

        recipe.save()  # Will do the SQL update query.

        return {"message": "Success"}, 200, None

    def delete(self):
        authorize(g.headers)
        data = request.get_json()

        try:
            recipe = Re.select().where(
                Re.uuid == g.args.get('uuid')).get()
        except Re.DoesNotExist:
            return {"message": "Recipe not found"}, 404, None
        ingredients = In.delete().where(In.recipe_id == recipe.id).execute()
        recipe.delete_instance()

        return {"message": "Success"}, 200, None
