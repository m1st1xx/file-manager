# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.11/lib-dynload/_testcapi.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .object import object

class HeapGcCType(object):
    """
    A heap type with GC, and with overridden dealloc.
    
    The 'value' attribute is set to 10 in __init__.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



