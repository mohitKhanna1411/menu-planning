from peewee import SqliteDatabase, Model, TextField, IntegerField, AutoField, DateTimeField, BlobField, ForeignKeyField
import os
from datetime import datetime


def create_db(db_file):

    if os.path.exists(db_file):
        print("Database already exists.")
        return False

    db = SqliteDatabase(db_file)

    class BaseTable(Model):
        class Meta:
            database = db

    class Users(BaseTable):
        id = AutoField()
        uuid = TextField(null=False)
        created_at = DateTimeField(default=datetime.now())
        username = TextField(null=False, unique=True)
        password = TextField(null=False)

    class Recipes(BaseTable):
        id = AutoField()
        user_id = ForeignKeyField(Users, backref='recipes')
        uuid = TextField(null=False)
        created_at = DateTimeField(default=datetime.now())
        name = TextField()
        steps = BlobField()
        classification = TextField()
        image = TextField()
        nutirtional_information = TextField()

    class Ingredients(BaseTable):
        id = AutoField()
        recipe_id = ForeignKeyField(Recipes, backref='ingredients')
        uuid = TextField(null=False)
        name = TextField()
        image = TextField()

    class MenuDetails(BaseTable):
        id = AutoField()
        uuid = TextField(null=False)
        week = IntegerField()
        year = IntegerField()
        description = TextField()

    class Menus(BaseTable):
        id = AutoField()
        uuid = TextField(null=False)
        menu_id = ForeignKeyField(MenuDetails, backref='menus')
        recipe_id = ForeignKeyField(Recipes, backref='menus')

    class Reviews(BaseTable):
        id = AutoField()
        uuid = TextField(null=False)
        ratings = IntegerField()
        comments = TextField()
        menu_id = ForeignKeyField(MenuDetails, backref='reviews')
        recipe_id = ForeignKeyField(Recipes, backref='reviews')
        customer_id = IntegerField()  # must be foregien key from customer table

    db.connect()
    db.create_tables([Users, Recipes, Ingredients, MenuDetails, Menus,Reviews])