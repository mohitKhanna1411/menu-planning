# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'

definitions = {'definitions': {'new_recipe_details': {'required': ['name', 'ingredients', 'steps', 'classification', 'nutirtional_information', 'image'], 'properties': {'name': {'type': 'string', 'example': 'aloo paranthe'}, 'ingredients': {'type': 'array', 'items': {'type': 'string'}, 'example': ['101-dasfda-dasdfad', '201-nfsnfnjk-fdasfa']}, 'method': {'type': 'string', 'example': 'step1,step2, there you go!'}, 'classification': {'type': 'string', 'enum': ['Breakfast', 'Brunch', 'Snack', 'Lunch', 'Tea', 'Supper', 'Dinner']}, 'nutirtional_information': {'type': 'string', 'example': 'some string'}, 'image': {'type': 'string', 'example': 'link to image'}}, 'type': 'object'}, 'recipe_details': {'properties': {'id': {'type': 'integer', 'example': 101}, 'image': {'type': 'string'}, 'name': {'type': 'string', 'example': 'aloo paranthe'}, 'steps': {'type': 'string', 'example': 'take aloo make paranthe'}, 'ingredients': {'type': 'array', 'items': {'type': 'string'}, 'example': ['21312', '123133']}, 'classification': {'type': 'string', 'example': 'Breakfast'}, 'nutirtional_information': {'type': 'string', 'example': 'some string'}}, 'type': 'object'}, 'recipe_id_details': {'properties': {'recipe_id': {'type': 'string'}}, 'type': 'object'}, 'new_comment_details': {'properties': {'comment': {'type': 'string', 'example': 'Awesome recipe!'}}, 'type': 'object'}, 'login_details': {'required': ['password', 'username'], 'properties': {'username': {'type': 'string', 'example': 'mohitkhanna'}, 'password': {'type': 'string', 'example': 'khanna1234'}}, 'type': 'object'}, 'token_details': {'properties': {'token': {'type': 'string'}}, 'type': 'object'}, 'message': {'type': 'object', 'properties': {'message': {'type': 'string', 'example': 'Success'}}}, 'signup_details': {'required': ['password', 'username'], 'properties': {'username': {'type': 'string', 'example': 'mohitkhanna'}, 'password': {'type': 'string', 'example': 'khanna1234'}}, 'type': 'object'}}, 'parameters': {}}

validators = {
    ('auth_login', 'POST'): {'json': {'$ref': '#/definitions/login_details'}},
    ('auth_signup', 'POST'): {'json': {'$ref': '#/definitions/signup_details'}},
    ('recipe', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to delete', 'type': 'string'}}}},
    ('recipe', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to fetch', 'type': 'string'}}}},
    ('recipe', 'POST'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('recipe', 'PUT'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to update', 'type': 'string'}}}},
    ('recipe_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'name': {'description': 'the name of the recipe to fetch', 'type': 'string'}, 'method': {'description': 'the method of the recipe to fetch', 'type': 'string'}, 'meal_type': {'description': 'the meal_type of the recipe to fetch', 'type': 'string'}, 'ingredients': {'description': 'the ingredients of the recipe to fetch', 'type': 'string'}}}},
    ('menu', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the menu to delete', 'type': 'string'}}}},
    ('menu', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to fetch', 'type': 'string'}}}},
    ('menu', 'POST'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('menu', 'PUT'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to update', 'type': 'string'}}}},
    ('menu_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'name': {'description': 'the name of the recipe to fetch', 'type': 'string'}, 'method': {'description': 'the method of the recipe to fetch', 'type': 'string'}, 'meal_type': {'description': 'the meal_type of the recipe to fetch', 'type': 'string'}, 'ingredients': {'description': 'the ingredients of the recipe to fetch', 'type': 'string'}}}},
    ('ingredients', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the ingredients to delete', 'type': 'string'}}}},
    ('ingredients', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to fetch', 'type': 'string'}}}},
    ('ingredients', 'POST'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('ingredients', 'PUT'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to update', 'type': 'string'}}}},
    ('ingredients_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'name': {'description': 'the name of the recipe to fetch', 'type': 'string'}, 'method': {'description': 'the method of the recipe to fetch', 'type': 'string'}, 'meal_type': {'description': 'the meal_type of the recipe to fetch', 'type': 'string'}, 'ingredients': {'description': 'the ingredients of the recipe to fetch', 'type': 'string'}}}},
    ('review', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the menu to delete', 'type': 'string'}}}},
    ('review', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to fetch', 'type': 'string'}}}},
    ('review', 'POST'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('review', 'PUT'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'id': {'description': 'the id of the recipe to update', 'type': 'string'}}}},
    ('review_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'name': {'description': 'the name of the recipe to fetch', 'type': 'string'}, 'method': {'description': 'the method of the recipe to fetch', 'type': 'string'}, 'meal_type': {'description': 'the meal_type of the recipe to fetch', 'type': 'string'}, 'ingredients': {'description': 'the ingredients of the recipe to fetch', 'type': 'string'}}}},
}

filters = {
    ('auth_login', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/token_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('auth_signup', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/token_details'}}, 400: {'headers': None, 'schema': None}, 409: {'headers': None, 'schema': None}},
    ('recipe', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('recipe', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('recipe', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_id_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('recipe', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('recipe_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('menu', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('menu', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('menu', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_id_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('menu', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('menu_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('ingredients', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('ingredients', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('ingredients', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_id_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('ingredients', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('ingredients_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('review', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('review', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('review', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_id_details'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('review', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('review_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 400: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
