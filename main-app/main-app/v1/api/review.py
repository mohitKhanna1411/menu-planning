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
        menu_uuid = ''
        review_uuid = ''
        try:
            review = Rev.select().where(Rev.uuid == uuid).dicts().get()
        except Rev.DoesNotExist:
            return {"message": "Review not found"}, 404, None
        if review['review_type'] == 'Menu':
            menu_uuid = Me.select(Me.uuid).where(
                Me.id == review['menu_id']).dicts().get()
            menu_uuid = menu_uuid['uuid']
        elif review['review_type'] == 'Recipe':
            review_uuid = Re.select(Re.uuid).where(
                Re.id == review['recipe_id']).dicts().get()
            review_uuid = review_uuid['uuid']

        return {
            'id': review['id'],
            'uuid': review['uuid'],
            'ratings': review['ratings'],
            'comments': review['comments'],
            'type': review['review_type'],
            'menu_id': menu_uuid,
            'recipe_id': review_uuid,
            'customer_id': review['customer_id'],
        }, 200, None

    def post(self):
        authorize(g.headers)
        data = request.get_json()
        uniquie_uuid = str(uuid.uuid4())
        menu_id = ''
        recipe_id = ''

        if data.get('type') == 'Menu':
            try:
                menu_id = Me.select(Me.id).where(
                    Me.uuid == data.get('menu_id')).dicts().get()
                menu_id = menu_id['id']
            except Me.DoesNotExist:
                return {"message": "Menu not found"}, 400, None
        elif data.get('type') == 'Recipe':
            try:
                recipe_id = Re.select(Re.id).where(
                    Re.uuid == data.get('recipe_id')).dicts().get()
                recipe_id = recipe_id['id']
            except Re.DoesNotExist:
                return {"message": "Recipe not found"}, 400, None
        Rev.create(
            uuid=uniquie_uuid,
            ratings=data.get('ratings'),
            comments=data.get('comments'),
            review_type=data.get('type'),
            menu_id=menu_id,
            recipe_id=recipe_id,
            customer_id=data.get('customer_id'),
        )
        review = Rev.select().where(Rev.uuid == uniquie_uuid).dicts().get()
        print(review, flush=True)
        return {'id': review['id'],
                'uuid': review['uuid'],
                'ratings': review['ratings'],
                'type': review['review_type'],
                'comments': review['comments'],
                'menu_id': data.get('menu_id'),
                'recipe_id': data.get('recipe_id'),
                }, 201, None

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
