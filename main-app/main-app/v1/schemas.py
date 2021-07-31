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

definitions = {'definitions': {'new_recipe_details': {'required': ['name', 'steps', 'classification', 'nutirtional_information', 'image', 'ingredients'], 'properties': {'name': {'type': 'string', 'example': 'sandwich'}, 'steps': {'type': 'string', 'example': 'step1,step2, there you go!'}, 'classification': {'type': 'string', 'enum': ['Breakfast', 'Brunch', 'Snack', 'Lunch', 'Tea', 'Supper', 'Dinner']}, 'nutirtional_information': {'type': 'string', 'example': 'some string'}, 'image': {'type': 'string', 'example': 'link to image'}, 'ingredients': {'type': 'array', 'items': {'$ref': '#/definitions/ingredients'}}}, 'type': 'object'}, 'recipe_details': {'properties': {'id': {'type': 'integer', 'example': 101}, 'uuid': {'type': 'string', 'example': '21321j3123j-3n123-3123'}, 'image': {'type': 'string'}, 'name': {'type': 'string', 'example': 'sandwich'}, 'ingredients': {'type': 'array', 'items': {'$ref': '#/definitions/ingredients'}}, 'steps': {'type': 'string', 'example': 'take bread make sandwich'}, 'classification': {'type': 'string', 'example': 'Breakfast'}, 'nutirtional_information': {'type': 'string', 'example': 'some string'}}, 'type': 'object'}, 'ingredients': {'type': 'object', 'properties': {'name': {'type': 'string', 'example': 'bread'}, 'image': {'type': 'string', 'example': 'link_image_'}}}, 'login_details': {'required': ['password', 'username'], 'properties': {'username': {'type': 'string', 'example': 'mohitkhanna'}, 'password': {'type': 'string', 'example': 'khanna1234'}}, 'type': 'object'}, 'token_details': {'properties': {'token': {'type': 'string'}}, 'type': 'object'}, 'review_details': {'properties': {'id': {'type': 'integer', 'example': 101}, 'uuid': {'type': 'string', 'example': '21321j3123j-3n123-3123'}, 'ratings': {'type': 'integer', 'example': 4}, 'comments': {'type': 'string', 'example': 'tasty!'}, 'menu_id': {'type': 'string', 'example': '21312321-4221-fefe-11'}, 'recipe_id': {'type': 'string', 'example': 'dadfsd1221-4221-fefe-11'}, 'customer_id': {'type': 'string', 'example': 'dadfsd1221-4221-fefe-11'}}, 'type': 'object'}, 'review_details_body': {'properties': {'ratings': {'type': 'integer', 'example': 4}, 'comments': {'type': 'string', 'example': 'tasty!'}, 'menu_id': {'type': 'string', 'example': '21312321-4221-fefe-11'}, 'recipe_id': {'type': 'string', 'example': 'dadfsd1221-4221-fefe-11'}, 'customer_id': {'type': 'string', 'example': 'dadfsd1221-4221-fefe-11'}}, 'type': 'object'}, 'menu_details': {'properties': {'id': {'type': 'integer', 'example': 101}, 'uuid': {'type': 'string', 'example': '21321j3123j-3n123-3123'}, 'description': {'type': 'string', 'example': 'menu for week1 feb'}, 'week': {'type': 'integer', 'example': 22}, 'year': {'type': 'integer', 'example': 2021}, 'recipes': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 'type': 'object'}, 'menu_details_body': {'properties': {'description': {'type': 'string', 'example': 'menu for week1 feb'}, 'week': {'type': 'integer', 'example': 22}, 'year': {'type': 'integer', 'example': 2021}, 'recipes': {'items': {'type': 'string'}, 'example': ['123123-rwr', '234213-gfsdfgf-12']}}, 'type': 'object'}, 'message': {'type': 'object', 'properties': {'message': {'type': 'string', 'example': 'Success/Error message'}}}, 'signup_details': {'required': ['password', 'username'], 'properties': {'username': {'type': 'string', 'example': 'mohitkhanna'}, 'password': {'type': 'string', 'example': 'khanna1234'}}, 'type': 'object'}}, 'parameters': {}}

validators = {
    ('auth_login', 'POST'): {'json': {'$ref': '#/definitions/login_details'}},
    ('auth_signup', 'POST'): {'json': {'$ref': '#/definitions/signup_details'}},
    ('recipe', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to delete', 'type': 'string'}}}},
    ('recipe', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to fetch', 'type': 'string'}}}},
    ('recipe', 'POST'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('recipe', 'PUT'): {'json': {'$ref': '#/definitions/new_recipe_details'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to update', 'type': 'string'}}}},
    ('recipe_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('menu', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the menu to delete', 'type': 'string'}}}},
    ('menu', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to fetch', 'type': 'string'}}}},
    ('menu', 'POST'): {'json': {'$ref': '#/definitions/menu_details_body'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('menu', 'PUT'): {'json': {'$ref': '#/definitions/menu_details_body'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to update', 'type': 'string'}}}},
    ('menu_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('review', 'DELETE'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the review to delete', 'type': 'string'}}}},
    ('review', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the recipe to fetch', 'type': 'string'}}}},
    ('review', 'POST'): {'json': {'$ref': '#/definitions/review_details_body'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
    ('review', 'PUT'): {'json': {'$ref': '#/definitions/review_details_body'}, 'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}, 'args': {'required': [], 'properties': {'uuid': {'description': 'the uuid of the review to update', 'type': 'string'}}}},
    ('review_list', 'GET'): {'headers': {'required': [], 'properties': {'Authorization': {'type': 'string', 'description': "Your Authorization Token in the form 'Token <AUTH_TOKEN>'"}}}},
}

filters = {
    ('auth_login', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/token_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('auth_signup', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/token_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('recipe', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('recipe', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('recipe', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/recipe_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('recipe', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('recipe_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/recipe_details'}}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('menu', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('menu', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/menu_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('menu', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/menu_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('menu', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('menu_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/menu_details'}}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('review', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('review', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/review_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('review', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/review_details'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('review', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
    ('review_list', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/review_details'}}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 403: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/message'}}},
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
