from peewee import SqliteDatabase, Model, TextField, IntegerField, AutoField, DateTimeField, BlobField, ForeignKeyField
import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
DB_NAME = os.environ.get("DB_NAME")
db = SqliteDatabase(DB_NAME)

# basetable


class BaseTable(Model):
    class Meta:
        database = db

# Users inheriting basetable
# Users table defination


class Users(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    created_at = DateTimeField(default=datetime.now())
    username = TextField(null=False, unique=True)
    password = TextField(null=False)

# Recipes table defination
# Recipes inheriting basetable


class Recipes(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    created_at = DateTimeField(default=datetime.now())
    name = TextField()
    steps = BlobField()
    classification = TextField()
    image = TextField()
    nutirtional_information = TextField()

# Ingredients table defination
# Ingredients inheriting basetable


class Ingredients(BaseTable):
    id = AutoField()
    recipe_id = ForeignKeyField(Recipes, backref='ingredients')
    uuid = TextField(null=False)
    name = TextField()
    image = TextField()

# MenuDetails table defination
# MenuDetails inheriting basetable


class MenuDetails(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    week = IntegerField()
    year = IntegerField()
    description = TextField()

# Menus table defination
# Menus inheriting basetable


class Menus(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    menu_id = ForeignKeyField(MenuDetails, backref='menus')
    recipe_id = ForeignKeyField(Recipes, backref='menus')

# Reviews table defination
# Reviews inheriting basetable


class Reviews(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    ratings = IntegerField()
    comments = TextField()
    review_type = TextField()
    menu_id = ForeignKeyField(MenuDetails, backref='reviews')
    recipe_id = ForeignKeyField(Recipes, backref='reviews')
    customer_id = IntegerField()  # must be foregien key from customer table


def create_db(db_file):
    # check for file
    if os.path.exists(db_file):
        print("Database already exists.")
        return False
    # creating the tables
    db.connect()
    db.create_tables([Users, Recipes, Ingredients,
                      MenuDetails, Menus, Reviews])
