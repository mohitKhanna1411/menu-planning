import unittest
from peewee import SqliteDatabase
from flask import Flask
import os
from ..v1.models import Users, Recipes, Ingredients, MenuDetails, Menus, Reviews

app = Flask(__name__)

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = SqliteDatabase('test_hellofresh.db')
        self.db.connect()
        self.db.create_tables([Users, Recipes, Ingredients,
                               MenuDetails, Menus, Reviews])

    def tearDown(self):
        # Delete Database collections after the test is complete
        os.remove('test_hellofresh.db')
