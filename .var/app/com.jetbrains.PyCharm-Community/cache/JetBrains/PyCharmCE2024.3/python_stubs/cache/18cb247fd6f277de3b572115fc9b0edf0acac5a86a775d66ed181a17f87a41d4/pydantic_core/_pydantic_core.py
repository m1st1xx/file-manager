# encoding: utf-8
# module pydantic_core._pydantic_core
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/pydantic_core/_pydantic_core.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import datetime as __datetime


# Variables with simple values

build_info = 'profile=release pgo=false'
build_profile = 'release'

_recursion_limit = 255

__version__ = '2.41.5'

# functions

def from_json(*args, **kwargs): # real signature unknown
    pass

def list_all_errors(*args, **kwargs): # real signature unknown
    pass

def to_json(*args, **kwargs): # real signature unknown
    pass

def to_jsonable_python(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgsKwargs(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kwargs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class MultiHostUrl(object):
    # no doc
    @classmethod
    def build(cls, *args, **kwargs): # real signature unknown
        pass

    def hosts(self, *args, **kwargs): # real signature unknown
        pass

    def query_params(self, *args, **kwargs): # real signature unknown
        pass

    def unicode_string(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PydanticCustomError(ValueError):
    # no doc
    def message(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_template = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PydanticKnownError(ValueError):
    # no doc
    def message(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_template = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PydanticOmit(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class PydanticSerializationError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class PydanticSerializationUnexpectedValue(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class PydanticUndefinedType(object):
    # no doc
    def new(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class PydanticUseDefault(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class SchemaError(Exception):
    # no doc
    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def error_count(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class SchemaSerializer(object):
    # no doc
    def to_json(self, *args, **kwargs): # real signature unknown
        pass

    def to_python(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class SchemaValidator(object):
    # no doc
    def get_default_value(self, *args, **kwargs): # real signature unknown
        pass

    def isinstance_python(self, *args, **kwargs): # real signature unknown
        pass

    def validate_assignment(self, *args, **kwargs): # real signature unknown
        pass

    def validate_json(self, *args, **kwargs): # real signature unknown
        pass

    def validate_python(self, *args, **kwargs): # real signature unknown
        pass

    def validate_strings(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Some(object):
    # no doc
    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __match_args__ = (
        'value',
    )


class TzInfo(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class Url(object):
    # no doc
    @classmethod
    def build(cls, *args, **kwargs): # real signature unknown
        pass

    def query_params(self, *args, **kwargs): # real signature unknown
        pass

    def unicode_host(self, *args, **kwargs): # real signature unknown
        pass

    def unicode_string(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ValidationError(ValueError):
    # no doc
    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def error_count(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def from_exception_data(cls, *args, **kwargs): # real signature unknown
        pass

    def json(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

PydanticUndefined = None # (!) real value is 'PydanticUndefined'

__all__ = [
    'from_json',
    'list_all_errors',
    'to_json',
    'to_jsonable_python',
    'ArgsKwargs',
    'MultiHostUrl',
    'Some',
    'Url',
    'PydanticCustomError',
    'PydanticKnownError',
    'PydanticOmit',
    'PydanticSerializationError',
    'PydanticSerializationUnexpectedValue',
    'PydanticUndefinedType',
    'PydanticUseDefault',
    'SchemaError',
    'SchemaSerializer',
    'SchemaValidator',
    'TzInfo',
    'ValidationError',
    '__version__',
    'build_profile',
    'build_info',
    '_recursion_limit',
    'PydanticUndefined',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38e06d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pydantic_core._pydantic_core', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38e06d0>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/pydantic_core/_pydantic_core.cpython-311-x86_64-linux-gnu.so')"

