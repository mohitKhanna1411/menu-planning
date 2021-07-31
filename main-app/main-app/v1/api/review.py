# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Reviews as Rev, Recipes as Re, MenuDetails as Me
from ..helpers import authorize
from . import Resource
from .. import schemas


class Review(Resource):

    def get(self):
        authorize(g.headers)
        uuid = g.args.get('uuid')
        print(uuid, flush=True)
        try:
            review = Rev.select().where(Rev.uuid == uuid).dicts().get()
        except Rev.DoesNotExist:
            return {"message": "Review not found"}, 404, None
        if review['menu_id']:
            menu_uuid = Me.select(Me.uuid).where(
                Me.id == review['menu_id']).dicts().get()
        elif review['recipe_id']:
            review_uuid = Re.select(Re.uuid).where(
                Re.id == review['recipe_id']).dicts().get()
        return {
            'id': review['id'],
            'uuid': review['uuid'],
            'ratings': review['ratings'],
            'comments': review['comments'],
            'menu_id': menu_uuid,
            'recipe_id': review_uuid,
            'customer_id': review['customer_id'],
        }, 200, None

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
