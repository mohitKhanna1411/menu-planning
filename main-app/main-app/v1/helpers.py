from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
from .models import Users
import os
import jwt
from flask_restplus import abort

load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get("SECRET_KEY")


def gen_token(public_id):
    return jwt.encode({
        'public_id': public_id,
        'exp': datetime.utcnow() + timedelta(minutes=120)
    }, SECRET_KEY, algorithm="HS256")


def authorize(headers):
    t = headers.get('Authorization', None)
    if not t:
        abort(403, 'Unsupplied Authorization Token')
    if t.split(" ")[0] != "Token":
        abort(400, "Authorization Token must start with 'Token'")
    try:
        t = t.split(" ")[1]
    except:
        abort(403, "Unsupplied Authorization Token")

    print(t, SECRET_KEY)
    try:
        data = jwt.decode(t, SECRET_KEY, algorithms=["HS256"])
    except:
        abort(401, "Token Expired")
    user = Users.select().where(Users.uuid == data['uuid'])
    if not user:
        abort(404, 'User Not Found')
    print(user, flush=True)
    return user
