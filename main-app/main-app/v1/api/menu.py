# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from ..models import Recipes as Re, Ingredients as In, Menus as Ms, MenuDetails as Me
from flask import request, g
from ..helpers import authorize
import uuid

from . import Resource
from .. import schemas


class Menu(Resource):

    def get(self):
        authorize(g.headers)
        uuid = g.args.get('uuid')
        print(uuid, flush=True)
        try:
            menu = Me.select().where(Me.uuid == uuid).dicts().get()
        except Me.DoesNotExist:
            return {"message": "Menu not found"}, 404, None
        menu_s = Ms.select().where(
            Ms.menu_id == menu['id'])
        # print("menu_s-----", flush=True)
        # print(menu_s, flush=True)
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

        result = {
            "id": menu['id'],
            "uuid": menu['uuid'],
            "week": menu['week'],
            "year": menu['year'],
            "description": menu['description'],
            "recipes": r_res
        }
        print(result, flush=True)
        return result, 200, None

    def post(self):
        authorize(g.headers)
        data = request.get_json()

        # print(data, flush=True)
        uniquie_uuid = str(uuid.uuid4())
        Me.create(
            uuid=uniquie_uuid,
            week=data.get('week'),
            year=data.get('year'),
            description=data.get('description'),
        )
        menu_id = Me.select(Me.id).where(Me.uuid == uniquie_uuid).dicts().get()
        # print("menu_id-----", flush=True)
        # print(menu_id['id'], flush=True)
        for r in data.get('recipes'):

            try:
                recipe_id = Re.select(Re.id).where(Re.uuid == r).dicts().get()
            except Re.DoesNotExist:
                return {"message": "Recipe not found"}, 400, None

            # print("recipe_id-----", flush=True)
            # print(recipe_id['id'], flush=True)

            Ms.create(
                uuid=str(uuid.uuid4()),
                recipe_id=recipe_id['id'],
                menu_id=menu_id['id'],
            )
        return {'id': menu_id['id'],
                'uuid': uniquie_uuid,
                'week': data.get('week'),
                'year': data.get('year'),
                'description': data.get('description'),
                }, 201, None

    def put(self):
        authorize(g.headers)
        data = request.get_json()
        try:
            menu = Me.select().where(
                Me.uuid == g.args.get('uuid')).get()
        except Me.DoesNotExist:
            return {"message": "Menu not found"}, 404, None
        # print(data, flush=True)
        menu.week = data.get('week')
        menu.year = data.get('year')
        menu.description = data.get('description')

        menu.save()  # Will do the SQL update query.

        return {"message": "Success"}, 200, None

    def delete(self):
        authorize(g.headers)
        data = request.get_json()

        try:
            menu = Me.select().where(
                Me.uuid == g.args.get('uuid')).get()
        except Me.DoesNotExist:
            return {"message": "Menu not found"}, 404, None
        menu_s = Ms.delete().where(Ms.menu_id == menu.id).execute()
        menu.delete_instance()

        return {"message": "Success"}, 200, None
