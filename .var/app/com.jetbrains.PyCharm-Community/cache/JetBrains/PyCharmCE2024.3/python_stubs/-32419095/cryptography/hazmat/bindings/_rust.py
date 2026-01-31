# encoding: utf-8
# module cryptography.hazmat.bindings._rust
# from /app/lib/python3.11/site-packages/cryptography/hazmat/bindings/_rust.abi3.so
# by generator 1.147
# no doc

# imports
import asn1 as asn1 # <module 'asn1'>
import pkcs7 as pkcs7 # <module 'pkcs7'>
import x509 as x509 # <module 'x509'>
import ocsp as ocsp # <module 'ocsp'>

# functions

def check_ansix923_padding(*args, **kwargs): # real signature unknown
    pass

def check_pkcs7_padding(*args, **kwargs): # real signature unknown
    pass

# classes

class FixedPool(object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectIdentifier(object):
    # no doc
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    dotted_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'check_pkcs7_padding',
    'check_ansix923_padding',
    'ObjectIdentifier',
    'FixedPool',
    'asn1',
    'pkcs7',
    'x509',
    'ocsp',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8ad2d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='cryptography.hazmat.bindings._rust', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8ad2d0>, origin='/app/lib/python3.11/site-packages/cryptography/hazmat/bindings/_rust.abi3.so')"

