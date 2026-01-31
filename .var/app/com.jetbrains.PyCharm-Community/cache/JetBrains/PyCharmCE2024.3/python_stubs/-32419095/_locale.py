# encoding: utf-8
# module _locale
# from (built-in)
# by generator 1.147
""" Support for POSIX locales. """
# no imports

# Variables with simple values

ABDAY_1 = 131072
ABDAY_2 = 131073
ABDAY_3 = 131074
ABDAY_4 = 131075
ABDAY_5 = 131076
ABDAY_6 = 131077
ABDAY_7 = 131078

ABMON_1 = 131086
ABMON_10 = 131095
ABMON_11 = 131096
ABMON_12 = 131097
ABMON_2 = 131087
ABMON_3 = 131088
ABMON_4 = 131089
ABMON_5 = 131090
ABMON_6 = 131091
ABMON_7 = 131092
ABMON_8 = 131093
ABMON_9 = 131094

ALT_DIGITS = 131119

AM_STR = 131110

CHAR_MAX = 127

CODESET = 14

CRNCYSTR = 262159

DAY_1 = 131079
DAY_2 = 131080
DAY_3 = 131081
DAY_4 = 131082
DAY_5 = 131083
DAY_6 = 131084
DAY_7 = 131085

D_FMT = 131113

D_T_FMT = 131112

ERA = 131116

ERA_D_FMT = 131118

ERA_D_T_FMT = 131120

ERA_T_FMT = 131121

LC_ALL = 6
LC_COLLATE = 3
LC_CTYPE = 0
LC_MESSAGES = 5
LC_MONETARY = 4
LC_NUMERIC = 1
LC_TIME = 2

MON_1 = 131098
MON_10 = 131107
MON_11 = 131108
MON_12 = 131109
MON_2 = 131099
MON_3 = 131100
MON_4 = 131101
MON_5 = 131102
MON_6 = 131103
MON_7 = 131104
MON_8 = 131105
MON_9 = 131106

NOEXPR = 327681

PM_STR = 131111

RADIXCHAR = 65536

THOUSEP = 65537

T_FMT = 131114

T_FMT_AMPM = 131115

YESEXPR = 327680

_DATE_FMT = 131180

# functions

def bindtextdomain(*args, **kwargs): # real signature unknown
    """ Bind the C library's domain to dir. """
    pass

def bind_textdomain_codeset(*args, **kwargs): # real signature unknown
    """ Bind the C library's domain to codeset. """
    pass

def dcgettext(*args, **kwargs): # real signature unknown
    """ Return translation of msg in domain and category. """
    pass

def dgettext(domain, msg): # real signature unknown; restored from __doc__
    """
    dgettext(domain, msg) -> string
    
    Return translation of msg in domain.
    """
    return ""

def getencoding(*args, **kwargs): # real signature unknown
    """ Get the current locale encoding. """
    pass

def gettext(msg): # real signature unknown; restored from __doc__
    """
    gettext(msg) -> string
    
    Return translation of msg.
    """
    return ""

def localeconv(*args, **kwargs): # real signature unknown
    """ Returns numeric and monetary locale-specific parameters. """
    pass

def nl_langinfo(*args, **kwargs): # real signature unknown
    """ Return the value for the locale information associated with key. """
    pass

def setlocale(*args, **kwargs): # real signature unknown
    """ Activates/queries locale processing. """
    pass

def strcoll(*args, **kwargs): # real signature unknown
    """ Compares two strings according to the locale. """
    pass

def strxfrm(*args, **kwargs): # real signature unknown
    """ Return a string that can be used as a key for locale-aware comparisons. """
    pass

def textdomain(*args, **kwargs): # real signature unknown
    """ Set the C library's textdmain to domain, returning the new domain. """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x7f25fb60e8e0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7f25fb60e980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x7f25fb60ea20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7f25fb60eac0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7f25fb60eb60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7f25fb60eca0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7f25fb60ede0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7f25fb60ef20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7f25fb60dc60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_locale', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

