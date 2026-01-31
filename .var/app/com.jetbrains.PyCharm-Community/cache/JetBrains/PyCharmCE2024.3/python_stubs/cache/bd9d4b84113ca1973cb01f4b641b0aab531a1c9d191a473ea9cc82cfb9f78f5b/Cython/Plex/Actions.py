# encoding: utf-8
# module Cython.Plex.Actions
# from /usr/lib/python3.11/site-packages/Cython/Plex/Actions.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# no functions
# classes

class Action(object):
    # no doc
    def same_as(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabcf90>'


class Begin(Action):
    """
    Begin(state_name) is a Plex action which causes the Scanner to
        enter the state |state_name|. See the docstring of Plex.Lexicon
        for more information.
    """
    def same_as(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, state_name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabe580>'


class Call(Action):
    """ Internal Plex action which causes a function to be called. """
    def same_as(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabe550>'


class Ignore(Action):
    """
    IGNORE is a Plex action which causes its associated token
        to be ignored. See the docstring of Plex.Lexicon  for more
        information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabe5b0>'


class Return(Action):
    """
    Internal Plex action which causes |value| to
        be returned as the value of the associated token
    """
    def same_as(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabe520>'


class Text(Action):
    """
    TEXT is a Plex action which causes the text of a token to
        be returned as the value of the token. See the docstring of
        Plex.Lexicon  for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabe610>'


# variables with complex values

IGNORE = None # (!) real value is 'IGNORE'

TEXT = None # (!) real value is 'TEXT'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacf090>'

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Plex.Actions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacf090>, origin='/usr/lib/python3.11/site-packages/Cython/Plex/Actions.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

