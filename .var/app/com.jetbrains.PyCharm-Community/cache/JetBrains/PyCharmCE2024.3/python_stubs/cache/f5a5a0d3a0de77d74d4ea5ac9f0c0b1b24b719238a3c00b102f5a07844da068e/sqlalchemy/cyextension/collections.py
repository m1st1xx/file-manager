# encoding: utf-8
# module sqlalchemy.cyextension.collections
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/collections.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import filterfalse

import collections.abc as __collections_abc


# functions

def unique_list(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IdentitySet(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_OrderedSet(*args, **kwargs): # real signature unknown
    pass

# classes

class Collection(__collections_abc.Sized, __collections_abc.Iterable, __collections_abc.Container):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __subclasshook__(cls, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x7ff7b44b2400>'
    __abstractmethods__ = frozenset({'__contains__', '__iter__', '__len__'})
    __slots__ = ()


class IdentitySet(object):
    """
    A set that considers only object id() for uniqueness.
    
        This strategy has edge cases for builtin types- it's possible to have
        two 'foo' strings in one of these sets, for example.  Use sparingly.
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def difference(self, *args, **kwargs): # real signature unknown
        pass

    def difference_update(self, *args, **kwargs): # real signature unknown
        pass

    def discard(self, *args, **kwargs): # real signature unknown
        pass

    def intersection(self, *args, **kwargs): # real signature unknown
        pass

    def intersection_update(self, *args, **kwargs): # real signature unknown
        pass

    def issubset(self, *args, **kwargs): # real signature unknown
        pass

    def issuperset(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        pass

    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        pass

    def union(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
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

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7ff7b38f4c60>'


class OrderedSet(set):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def difference(self, *args, **kwargs): # real signature unknown
        pass

    def difference_update(self, *args, **kwargs): # real signature unknown
        pass

    def discard(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def intersection(self, *args, **kwargs): # real signature unknown
        pass

    def intersection_update(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        pass

    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        pass

    def union(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7ff7b38f4c30>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38f8150>'

__spec__ = None # (!) real value is "ModuleSpec(name='sqlalchemy.cyextension.collections', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38f8150>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/collections.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

