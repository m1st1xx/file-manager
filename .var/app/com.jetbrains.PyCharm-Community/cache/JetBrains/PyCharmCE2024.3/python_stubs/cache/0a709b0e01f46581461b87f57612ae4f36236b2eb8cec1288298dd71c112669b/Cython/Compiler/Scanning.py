# encoding: utf-8
# module Cython.Compiler.Scanning
# from /usr/lib/python3.11/site-packages/Cython/Compiler/Scanning.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import Cython.Utils as Utils # /usr/lib/python3.11/site-packages/Cython/Utils.py
import Cython.Plex.Errors as __Cython_Plex_Errors
import Cython.Plex.Scanners as __Cython_Plex_Scanners


# Variables with simple values

debug_scanner = 0

scanner_debug_flags = 0

scanner_dump_file = None

trace_scanner = 0

# no functions
# classes

class CompileTimeScope(object):
    # no doc
    def declare(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_here(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    outer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SourceDescriptor(object):
    """ A SourceDescriptor should be considered immutable. """
    def get_escaped_description(self, *args, **kwargs): # real signature unknown
        pass

    def is_cython_file(self, *args, **kwargs): # real signature unknown
        pass

    def is_python_file(self, *args, **kwargs): # real signature unknown
        pass

    def set_file_type_from_name(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    filename = None
    _cmp_name = ''
    _escaped_description = None
    _file_type = 'pyx'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.Scanning', '__doc__': '\\n    A SourceDescriptor should be considered immutable.\\n    ', 'filename': None, '_file_type': 'pyx', '_escaped_description': None, '_cmp_name': '', '__str__': <cyfunction SourceDescriptor.__str__ at 0x7f25fa8c42b0>, 'set_file_type_from_name': <cyfunction SourceDescriptor.set_file_type_from_name at 0x7f25fa8c4450>, 'is_cython_file': <cyfunction SourceDescriptor.is_cython_file at 0x7f25fa8c4520>, 'is_python_file': <cyfunction SourceDescriptor.is_python_file at 0x7f25fa8c45f0>, 'get_escaped_description': <cyfunction SourceDescriptor.get_escaped_description at 0x7f25fa8c41e0>, '__gt__': <cyfunction SourceDescriptor.__gt__ at 0x7f25fa8c46c0>, '__lt__': <cyfunction SourceDescriptor.__lt__ at 0x7f25fa8c4790>, '__le__': <cyfunction SourceDescriptor.__le__ at 0x7f25fa8c4860>, '__copy__': <cyfunction SourceDescriptor.__copy__ at 0x7f25fa8c4930>, '__deepcopy__': <cyfunction SourceDescriptor.__deepcopy__ at 0x7f25fa8c4a00>, '__dict__': <attribute '__dict__' of 'SourceDescriptor' objects>, '__weakref__': <attribute '__weakref__' of 'SourceDescriptor' objects>})"


class FileSourceDescriptor(SourceDescriptor):
    """
    Represents a code source. A code source is a more generic abstraction
        for a "filename" (as sometimes the code doesn't come from a file).
        Instances of code sources are passed to Scanner.__init__ as the
        optional name argument and will be passed back when asking for
        the position()-tuple.
    """
    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_error_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_filenametable_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_lines(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass


class Method(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __name__ = 'Method'


class PyrexScanner(__Cython_Plex_Scanners.Scanner):
    # no doc
    def begin_string_action(self, *args, **kwargs): # real signature unknown
        pass

    def close_bracket_action(self, *args, **kwargs): # real signature unknown
        pass

    def commentline(self, *args, **kwargs): # real signature unknown
        pass

    def end_string_action(self, *args, **kwargs): # real signature unknown
        pass

    def enter_async(self, *args, **kwargs): # real signature unknown
        pass

    def eof_action(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def exit_async(self, *args, **kwargs): # real signature unknown
        pass

    def expect(self, *args, **kwargs): # real signature unknown
        pass

    def expected(self, *args, **kwargs): # real signature unknown
        pass

    def expect_dedent(self, *args, **kwargs): # real signature unknown
        pass

    def expect_indent(self, *args, **kwargs): # real signature unknown
        pass

    def expect_keyword(self, *args, **kwargs): # real signature unknown
        pass

    def expect_newline(self, *args, **kwargs): # real signature unknown
        pass

    def indentation_action(self, *args, **kwargs): # real signature unknown
        pass

    def newline_action(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def open_bracket_action(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def put_back(self, *args, **kwargs): # real signature unknown
        pass

    def strip_underscores(self, *args, **kwargs): # real signature unknown
        pass

    def unclosed_string_action(self, *args, **kwargs): # real signature unknown
        pass

    def unread(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    async_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bracket_nesting_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compile_time_env = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compile_time_eval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compile_time_expr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    included_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indentation_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indentation_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_python_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parse_comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    systring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    string_states = {
        '"': 'DQ_STRING',
        '"""': 'TDQ_STRING',
        "'": 'SQ_STRING',
        "'''": 'TSQ_STRING',
    }
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa885d10>'


class StringSourceDescriptor(SourceDescriptor):
    """
    Instances of this class can be used instead of a filenames if the
        code originates from a string object.
    """
    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_error_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_filenametable_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_lines(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass


class UnrecognizedInput(__Cython_Plex_Errors.PlexError):
    # no doc
    def __init__(self, scanner, state_name): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    position = None
    scanner = None
    state_name = None


# variables with complex values

pyx_reserved_words = [
    'global',
    'nonlocal',
    'def',
    'class',
    'print',
    'del',
    'pass',
    'break',
    'continue',
    'return',
    'raise',
    'import',
    'exec',
    'try',
    'except',
    'finally',
    'while',
    'if',
    'elif',
    'else',
    'for',
    'in',
    'assert',
    'and',
    'or',
    'not',
    'is',
    'lambda',
    'from',
    'yield',
    'with',
    'include',
    'ctypedef',
    'cdef',
    'cpdef',
    'cimport',
    'DEF',
    'IF',
    'ELIF',
    'ELSE',
]

py_reserved_words = [
    'global',
    'nonlocal',
    'def',
    'class',
    'print',
    'del',
    'pass',
    'break',
    'continue',
    'return',
    'raise',
    'import',
    'exec',
    'try',
    'except',
    'finally',
    'while',
    'if',
    'elif',
    'else',
    'for',
    'in',
    'assert',
    'and',
    'or',
    'not',
    'is',
    'lambda',
    'from',
    'yield',
    'with',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacee50>'

__pyx_capi__ = {
    'IDENT': None, # (!) real value is '<capsule object "PyObject *" at 0x7f25faabf390>'
    'any_string_prefix': None, # (!) real value is '<capsule object "PyObject *" at 0x7f25faabf330>'
    'get_lexicon': None, # (!) real value is '<capsule object "PyObject *(void)" at 0x7f25faabf3c0>'
    'initial_compile_time_env': None, # (!) real value is '<capsule object "PyObject *(void)" at 0x7f25faabf3f0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Compiler.Scanning', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacee50>, origin='/usr/lib/python3.11/site-packages/Cython/Compiler/Scanning.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

