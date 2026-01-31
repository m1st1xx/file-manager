# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.11/lib-dynload/_testcapi.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .HeapCType import HeapCType

class HeapCTypeSubclass(HeapCType):
    """
    Subclass of HeapCType, without GC.
    
    __init__ sets the 'value' attribute to 10 and 'value2' to 20.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    value2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



