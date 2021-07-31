# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Reviews as Rev, Recipes as Re, MenuDetails as Me
from ..helpers import authorize
import uuid
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
        authorize(g.headers)
        data = request.get_json()
        uniquie_uuid = str(uuid.uuid4())
        if data.get('menu_id'):
            menu_id = Me.select(Me.id).where(
                Me.uuid == data.get('menu_id')).dicts().get()
        elif data.get('recipe_id'):
            recipe_id = Re.select(Me.id).where(
                Re.uuid == data.get('recipe_id')).dicts().get()
        Rev.create(
            uuid=uniquie_uuid,
            ratings=data.get('ratings'),
            comments=data.get('comments'),
            menu_id=menu_id,
            recipe_id=recipe_id,
            customer_id=data.get('customer_id'),
        )
        review = Rev.select().where(Rev.uuid == uniquie_uuid).dicts().get()
        print(review, flush=True)
        return {'id': review['id'],
                'uuid': review['uuid'],
                'ratings': review['ratings'],
                'comments': review['comments'],
                'menu_id': data.get('menu_id'),
                'recipe_id': data.get('recipe_id'),
                }, 200, None

    def put(self):
        authorize(g.headers)
        data = request.get_json()
        try:
            review = Rev.select().where(
                Rev.uuid == g.args.get('uuid')).get()
        except Rev.DoesNotExist:
            return {"message": "Review not found"}, 404, None
        print(data, flush=True)
        review.ratings = data.get('ratings')
        review.comments = data.get('comments')

        review.save()  # Will do the SQL update query.

        return {"message": "Success"}, 200, None

    def delete(self):
        authorize(g.headers)
        data = request.get_json()

        try:
            review = Rev.select().where(
                Rev.uuid == g.args.get('uuid')).get()
        except Rev.DoesNotExist:
            return {"message": "Review not found"}, 404, None
        review.delete_instance()

        return {"message": "Success"}, 200, None
