# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Reviews as Rev, Recipes as Re, MenuDetails as Me
from ..helpers import authorize
from . import Resource
from .. import schemas


class ReviewList(Resource):

    def get(self):
        print(g.headers)
        authorize(g.headers)

        review = Rev.select().order_by(Rev.id)
        r_res = []
        for r in review:
            in_res = []
            menu_uuid = ""
            review_uuid = ""
            if r.menu_id:
                menu_uuid = Me.select(Me.uuid).where(
                    Me.id == review['menu_id']).dicts().get()
            elif r.recipe_id:
                review_uuid = Re.select(Re.uuid).where(
                    Re.id == review['recipe_id']).dicts().get()
            r_res.append({
                'id': r.id,
                'uuid': r.uuid,
                'ratings': r.ratings,
                'comments': r.comments,
                'menu_id': r.menu_id,
                'recipe_id': r.recipe_id,
                'customer_id': r.customer_id,
            })

        return r_res, 200, None
