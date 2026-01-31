# encoding: utf-8
# module sqlalchemy.cyextension.immutabledict
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/immutabledict.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _immutable_fn(*args, **kwargs): # real signature unknown
    pass

def _readonly_fn(*args, **kwargs): # real signature unknown
    pass

# classes

class immutabledict(dict):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def merge_with(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def popitem(self, *args, **kwargs): # real signature unknown
        pass

    def setdefault(self, *args, **kwargs): # real signature unknown
        pass

    def union(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ImmutableDictBase(dict):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def popitem(self, *args, **kwargs): # real signature unknown
        pass

    def setdefault(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def _immutable(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'sqlalchemy.cyextension.immutabledict', '_immutable': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, '__class_getitem__': <classmethod(<cyfunction ImmutableDictBase.__class_getitem__ at 0x7ff7b38cf040>)>, '__delitem__': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, '__setitem__': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, '__setattr__': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, 'clear': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, 'pop': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, 'popitem': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, 'setdefault': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, 'update': <cyfunction ImmutableDictBase._immutable at 0x7ff7b38cef80>, '__dict__': <attribute '__dict__' of 'ImmutableDictBase' objects>, '__weakref__': <attribute '__weakref__' of 'ImmutableDictBase' objects>, '__doc__': None})"


class ReadOnlyContainer(object):
    # no doc
    def _readonly(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        pass

    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38f9a90>'

__spec__ = None # (!) real value is "ModuleSpec(name='sqlalchemy.cyextension.immutabledict', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38f9a90>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/immutabledict.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

