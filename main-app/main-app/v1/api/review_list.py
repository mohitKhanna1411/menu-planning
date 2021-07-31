# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Reviews as Rev
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
            # print(r.menu_id or '', flush=True)
            # print(r.recipe_id or '', flush=True)
            print(type(r), flush=True)
            r_res.append({
                'id': r.id,
                'uuid': r.uuid,
                'ratings': r.ratings,
                'comments': r.comments,
                'type': r.review_type,
                'customer_id': r.customer_id
            })

        return r_res, 200, None
