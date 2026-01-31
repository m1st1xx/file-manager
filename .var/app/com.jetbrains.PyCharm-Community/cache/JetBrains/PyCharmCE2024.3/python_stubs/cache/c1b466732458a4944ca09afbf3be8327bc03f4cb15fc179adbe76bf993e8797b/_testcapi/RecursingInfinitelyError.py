# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.11/lib-dynload/_testcapi.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .Exception import Exception

class RecursingInfinitelyError(Exception):
    """ Instantiating this exception starts infinite recursion. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


