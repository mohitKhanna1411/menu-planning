# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from .. import schemas
from . import Resource
from ..models import Users
from ..helpers import gen_token
from flask import request, g
from werkzeug.security import generate_password_hash
import uuid


class AuthSignup(Resource):

    def post(self):
        data = request.get_json()
        if not data or not data.get('password') or not data.get('username'):
            return {'message': 'Username/Password Cannot be empty'}, 400, None

        user = Users.select().where(Users.username == data.get('username'))
        if not user:
            Users.create(
                uuid=str(uuid.uuid4()),
                username=data.get('username'),
                password=generate_password_hash(data.get('password'))
            )
            token = gen_token(str(uuid.uuid4()))
            return {'token': token}, 200, None
        else:
            return {'message': 'Username Taken'}, 409, None
