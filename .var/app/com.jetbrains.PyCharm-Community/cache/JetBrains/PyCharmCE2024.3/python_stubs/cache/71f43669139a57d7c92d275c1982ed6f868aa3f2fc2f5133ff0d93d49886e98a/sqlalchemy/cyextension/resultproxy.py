# encoding: utf-8
# module sqlalchemy.cyextension.resultproxy
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/resultproxy.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # /usr/lib/python3.11/operator.py

# functions

def operator(*args, **kwargs): # real signature unknown
    """
    Operator interface.
    
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.
    """
    pass

def rowproxy_reconstructor(*args, **kwargs): # real signature unknown
    pass

def tuplegetter(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseRow(object):
    # no doc
    def _get_by_key_impl_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def _to_tuple_instance(self, *args, **kwargs): # real signature unknown
        pass

    def _values_impl(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ Row objects are constructed by CursorResult objects. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _key_to_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7ff7b38f59b0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b3908290>'

__spec__ = None # (!) real value is "ModuleSpec(name='sqlalchemy.cyextension.resultproxy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b3908290>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/resultproxy.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

