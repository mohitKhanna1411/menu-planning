# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.auth_login import AuthLogin
from .api.auth_signup import AuthSignup
from .api.recipe import Recipe
from .api.recipe_list import RecipeList
from .api.menu import Menu
from .api.menu_list import MenuList
from .api.review import Review
from .api.review_list import ReviewList


routes = [
    dict(resource=AuthLogin, urls=['/auth/login'], endpoint='auth_login'),
    dict(resource=AuthSignup, urls=['/auth/signup'], endpoint='auth_signup'),
    dict(resource=Recipe, urls=['/recipe/'], endpoint='recipe'),
    dict(resource=RecipeList, urls=['/recipe/list'], endpoint='recipe_list'),
    dict(resource=Menu, urls=['/menu/'], endpoint='menu'),
    dict(resource=MenuList, urls=['/menu/list'], endpoint='menu_list'),
    dict(resource=Review, urls=['/review/'], endpoint='review'),
    dict(resource=ReviewList, urls=['/review/list'], endpoint='review_list'),
]