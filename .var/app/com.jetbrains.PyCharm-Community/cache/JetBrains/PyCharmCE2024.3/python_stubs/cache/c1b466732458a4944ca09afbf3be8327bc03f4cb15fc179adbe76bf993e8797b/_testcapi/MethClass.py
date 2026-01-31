# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.11/lib-dynload/_testcapi.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .object import object

class MethClass(object):
    """ Class with class methods to test calling conventions """
    @classmethod
    def meth_fastcall(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def meth_fastcall_keywords(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def meth_noargs(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def meth_o(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def meth_varargs(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def meth_varargs_keywords(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


