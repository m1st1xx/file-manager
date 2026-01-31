# encoding: utf-8
# module Cython.Tempita._tempita
# from /usr/lib/python3.11/site-packages/Cython/Tempita/_tempita.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
"""
A small templating language

This implements a small templating language.  This language implements
if/elif/else, for/continue/break, expressions, and blocks of Python
code.  The syntax is::

  {{any expression (function calls etc)}}
  {{any expression | filter}}
  {{for x in y}}...{{endfor}}
  {{if x}}x{{elif y}}y{{else}}z{{endif}}
  {{py:x=1}}
  {{py:
  def foo(bar):
      return 'baz'
  }}
  {{default var = default_value}}
  {{# comment}}

You use this with the ``Template`` class or the ``sub`` shortcut.
The ``Template`` class takes the template string and the name of
the template (for errors) and a default namespace.  Then (like
``string.Template``) you can call the ``tmpl.substitute(**kw)``
method to make a substitution (or ``tmpl.substitute(a_dict)``).

``sub(content, **kw)`` substitutes the template immediately.  You
can use ``__name='tmpl.html'`` to set the name of the template.

If there are syntax errors ``TemplateError`` will be raised.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # /usr/lib/python3.11/re/__init__.py
import sys as sys # <module 'sys' (built-in)>
import os as os # /usr/lib/python3.11/os.py
import tokenize as tokenize # /usr/lib/python3.11/tokenize.py
from _io import StringIO


# Variables with simple values

_fill_command_usage = '%prog [OPTIONS] TEMPLATE arg=value\n\nUse py:arg=value to set a Python value; otherwise all values are\nstrings.\n'

# functions

def coerce_text(v): # reliably restored by inspect
    # no doc
    pass

def Empty(*args, **kwargs): # real signature unknown
    pass

def fill_command(*args, **kwargs): # real signature unknown
    pass

def find_position(*args, **kwargs): # real signature unknown
    """ Given a string and index, return (line, column) """
    pass

def get_file_template(*args, **kwargs): # real signature unknown
    pass

def isolate_expression(*args, **kwargs): # real signature unknown
    pass

def is_unicode(obj): # reliably restored by inspect
    # no doc
    pass

def lex(hey): # real signature unknown; restored from __doc__
    """
    Lex a string into chunks:
    
            >>> lex('hey')
            ['hey']
            >>> lex('hey {{you}}')
            ['hey ', ('you', (1, 7))]
            >>> lex('hey {{')
            Traceback (most recent call last):
                ...
            TemplateError: No }} to finish last expression at line 1 column 7
            >>> lex('hey }}')
            Traceback (most recent call last):
                ...
            TemplateError: }} outside expression at line 1 column 7
            >>> lex('hey {{ {{')
            Traceback (most recent call last):
                ...
            TemplateError: {{ inside expression at line 1 column 10
    """
    pass

def next(iterator, default=None): # real signature unknown; restored from __doc__
    """
    next(iterator[, default])
    
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    """
    pass

def parse(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Parses a string into a kind of AST
    
            >>> parse('{{x}}')
            [('expr', (1, 3), 'x')]
            >>> parse('foo')
            ['foo']
            >>> parse('{{if x}}test{{endif}}')
            [('cond', (1, 3), ('if', (1, 3), 'x', ['test']))]
            >>> parse('series->{{for x in y}}x={{x}}{{endfor}}')
            ['series->', ('for', (1, 11), ('x',), 'y', ['x=', ('expr', (1, 27), 'x')])]
            >>> parse('{{for x, y in z:}}{{continue}}{{endfor}}')
            [('for', (1, 3), ('x', 'y'), 'z', [('continue', (1, 21))])]
            >>> parse('{{py:x=1}}')
            [('py', (1, 3), 'x=1')]
            >>> parse('{{if x}}a{{elif y}}b{{else}}c{{endif}}')
            [('cond', (1, 3), ('if', (1, 3), 'x', ['a']), ('elif', (1, 12), 'y', ['b']), ('else', (1, 23), None, ['c']))]
    
        Some exceptions::
    
            >>> parse('{{continue}}')
            Traceback (most recent call last):
                ...
            TemplateError: continue outside of for loop at line 1 column 3
            >>> parse('{{if x}}foo')
            Traceback (most recent call last):
                ...
            TemplateError: No {{endif}} at line 1 column 3
            >>> parse('{{else}}')
            Traceback (most recent call last):
                ...
            TemplateError: else outside of an if block at line 1 column 3
            >>> parse('{{if x}}{{for x in y}}{{endif}}{{endfor}}')
            Traceback (most recent call last):
                ...
            TemplateError: Unexpected endif at line 1 column 25
            >>> parse('{{if}}{{endif}}')
            Traceback (most recent call last):
                ...
            TemplateError: if with no expression at line 1 column 3
            >>> parse('{{for x y}}{{endfor}}')
            Traceback (most recent call last):
                ...
            TemplateError: Bad for (no "in") in 'x y' at line 1 column 3
            >>> parse('{{py:x=1\ny=2}}')
            Traceback (most recent call last):
                ...
            TemplateError: Multi-line py blocks must start with a newline at line 1 column 3
    """
    pass

def parse_cond(*args, **kwargs): # real signature unknown
    pass

def parse_def(*args, **kwargs): # real signature unknown
    pass

def parse_default(*args, **kwargs): # real signature unknown
    pass

def parse_expr(*args, **kwargs): # real signature unknown
    pass

def parse_for(*args, **kwargs): # real signature unknown
    pass

def parse_inherit(*args, **kwargs): # real signature unknown
    pass

def parse_one_cond(*args, **kwargs): # real signature unknown
    pass

def parse_signature(*args, **kwargs): # real signature unknown
    pass

def paste_script_template_renderer(*args, **kwargs): # real signature unknown
    pass

def sub(*args, **kwargs): # real signature unknown
    pass

def trim_lex(tokens): # real signature unknown; restored from __doc__
    """
    Takes a lexed set of tokens, and removes whitespace when there is
        a directive on a line by itself:
    
           >>> tokens = lex('{{if x}}\nx\n{{endif}}\ny', trim_whitespace=False)
           >>> tokens
           [('if x', (1, 3)), '\nx\n', ('endif', (3, 3)), '\ny']
           >>> trim_lex(tokens)
           [('if x', (1, 3)), 'x\n', ('endif', (3, 3)), 'y']
    """
    pass

# classes

class bunch(dict):
    # no doc
    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._tempita', '__init__': <cyfunction bunch.__init__ at 0x7f25faaba810>, '__setattr__': <cyfunction bunch.__setattr__ at 0x7f25faaba8e0>, '__getattr__': <cyfunction bunch.__getattr__ at 0x7f25faaba9b0>, '__getitem__': <cyfunction bunch.__getitem__ at 0x7f25faabaa80>, '__repr__': <cyfunction bunch.__repr__ at 0x7f25faabac20>, '__dict__': <attribute '__dict__' of 'bunch' objects>, '__weakref__': <attribute '__weakref__' of 'bunch' objects>, '__doc__': None})"


class bytes(object):
    """
    bytes(iterable_of_ints) -> bytes
    bytes(string, encoding[, errors]) -> bytes
    bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object
    
    Construct an immutable array of bytes from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - any object implementing the buffer API.
      - an integer
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        B.capitalize() -> copy of B
        
        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character.
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs): # real signature unknown
        """
        Decode the bytes using the codec registered for encoding.
        
          encoding
            The encoding with which to decode the bytes.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.endswith(suffix[, start[, end]]) -> bool
        
        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.find(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a bytes object from a string of hexadecimal numbers.
        
        Spaces between two numbers are accepted.
        Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        Create a string of hexadecimal numbers from a bytes object.
        
          sep
            An optional single character or byte to separate hex bytes.
          bytes_per_sep
            How many bytes between separators.  Positive values count from the
            right, negative values count from the left.
        
        Example:
        >>> value = b'\xb9\x01\xef'
        >>> value.hex()
        'b901ef'
        >>> value.hex(':')
        'b9:01:ef'
        >>> value.hex(':', 2)
        'b9:01ef'
        >>> value.hex(':', -2)
        'b901:ef'
        """
        pass

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.index(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the subsection is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        B.isalnum() -> bool
        
        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        B.isalpha() -> bool
        
        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isascii(self): # real signature unknown; restored from __doc__
        """
        B.isascii() -> bool
        
        Return True if B is empty or all characters in B are ASCII,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        B.isdigit() -> bool
        
        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        B.islower() -> bool
        
        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        B.isspace() -> bool
        
        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        B.istitle() -> bool
        
        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        B.isupper() -> bool
        
        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Concatenate any number of bytes objects.
        
        The bytes whose method is called is inserted in between each pair.
        
        The result is returned as a new bytes object.
        
        Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character.
        """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """
        B.lower() -> copy of B
        
        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading bytes contained in the argument.
        
        If the argument is omitted or None, strip leading  ASCII whitespace.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table useable for the bytes or bytearray translate method.
        
        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.
        
        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original bytes
        object and two empty bytes objects.
        """
        pass

    def removeprefix(self, *args, **kwargs): # real signature unknown
        """
        Return a bytes object with the given prefix string removed if present.
        
        If the bytes starts with the prefix string, return bytes[len(prefix):].
        Otherwise, return a copy of the original bytes.
        """
        pass

    def removesuffix(self, *args, **kwargs): # real signature unknown
        """
        Return a bytes object with the given suffix string removed if present.
        
        If the bytes ends with the suffix string and that suffix is not empty,
        return bytes[:-len(prefix)].  Otherwise, return a copy of the original
        bytes.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character.
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty bytes
        objects and the original bytes object.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splitting is done starting at the end of the bytes and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the bytes, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.startswith(prefix[, start[, end]]) -> bool
        
        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading and trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        B.swapcase() -> copy of B
        
        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """
        B.title() -> copy of B
        
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with each character mapped by the given translation table.
        
          table
            Translation table, which must be a bytes object of length 256.
        
        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self): # real signature unknown; restored from __doc__
        """
        B.upper() -> copy of B
        
        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The original string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bytes__(self, *args, **kwargs): # real signature unknown
        """ Convert this value to exact type bytes. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, iterable_of_ints): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class looper(object):
    """
    Helper for looping (particularly in templates)
    
        Use this like::
    
            for loop, item in looper(seq):
                if loop.first:
                    ...
    """
    def __init__(self, seq): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._looper', '__doc__': '\\n    Helper for looping (particularly in templates)\\n\\n    Use this like::\\n\\n        for loop, item in looper(seq):\\n            if loop.first:\\n                ...\\n    ', '__init__': <function looper.__init__ at 0x7f25faac99e0>, '__iter__': <function looper.__iter__ at 0x7f25faac9da0>, '__repr__': <function looper.__repr__ at 0x7f25faac9e40>, '__dict__': <attribute '__dict__' of 'looper' objects>, '__weakref__': <attribute '__weakref__' of 'looper' objects>})"


class Template(object):
    # no doc
    @classmethod
    def from_filename(cls, *args, **kwargs): # real signature unknown
        pass

    def substitute(self, *args, **kwargs): # real signature unknown
        pass

    def _add_line_info(self, *args, **kwargs): # real signature unknown
        pass

    def _eval(self, *args, **kwargs): # real signature unknown
        pass

    def _exec(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_code(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_codes(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_for(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_if(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_inherit(self, *args, **kwargs): # real signature unknown
        pass

    def _repr(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    default_encoding = 'utf8'
    default_inherit = None
    default_namespace = {
        'end_braces': '}}',
        'looper': looper,
        'start_braces': '{{',
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._tempita', 'default_namespace': {'start_braces': '{{', 'end_braces': '}}', 'looper': <class 'Cython.Tempita._looper.looper'>}, 'default_encoding': 'utf8', 'default_inherit': None, '__init__': <cyfunction Template.__init__ at 0x7f25faab9b10>, 'from_filename': <classmethod(<cyfunction Template.from_filename at 0x7f25faab9cb0>)>, '__repr__': <cyfunction Template.__repr__ at 0x7f25faab9d80>, 'substitute': <cyfunction Template.substitute at 0x7f25faab9e50>, '_interpret': <cyfunction Template._interpret at 0x7f25faab9f20>, '_interpret_inherit': <cyfunction Template._interpret_inherit at 0x7f25faab9ff0>, '_interpret_codes': <cyfunction Template._interpret_codes at 0x7f25faab9be0>, '_interpret_code': <cyfunction Template._interpret_code at 0x7f25faaba0c0>, '_interpret_for': <cyfunction Template._interpret_for at 0x7f25faaba190>, '_interpret_if': <cyfunction Template._interpret_if at 0x7f25faaba260>, '_eval': <cyfunction Template._eval at 0x7f25faaba330>, '_exec': <cyfunction Template._exec at 0x7f25faaba400>, '_repr': <cyfunction Template._repr at 0x7f25faaba4d0>, '_add_line_info': <cyfunction Template._add_line_info at 0x7f25faaba5a0>, '__dict__': <attribute '__dict__' of 'Template' objects>, '__weakref__': <attribute '__weakref__' of 'Template' objects>, '__doc__': None})"


class TemplateDef(object):
    # no doc
    def _parse_signature(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._tempita', '__init__': <cyfunction TemplateDef.__init__ at 0x7f25faabab50>, '__repr__': <cyfunction TemplateDef.__repr__ at 0x7f25faabadc0>, '__str__': <cyfunction TemplateDef.__str__ at 0x7f25faabae90>, '__call__': <cyfunction TemplateDef.__call__ at 0x7f25faabaf60>, '__get__': <cyfunction TemplateDef.__get__ at 0x7f25faabb100>, '_parse_signature': <cyfunction TemplateDef._parse_signature at 0x7f25faabb1d0>, '__dict__': <attribute '__dict__' of 'TemplateDef' objects>, '__weakref__': <attribute '__weakref__' of 'TemplateDef' objects>, '__doc__': None})"


class TemplateError(Exception):
    """ Exception raised while parsing a template """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class TemplateObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._tempita', '__init__': <cyfunction TemplateObject.__init__ at 0x7f25faabb030>, '__repr__': <cyfunction TemplateObject.__repr__ at 0x7f25faabb2a0>, '__dict__': <attribute '__dict__' of 'TemplateObject' objects>, '__weakref__': <attribute '__weakref__' of 'TemplateObject' objects>, '__doc__': None})"


class TemplateObjectGetter(object):
    # no doc
    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Tempita._tempita', '__init__': <cyfunction TemplateObjectGetter.__init__ at 0x7f25faabb440>, '__getattr__': <cyfunction TemplateObjectGetter.__getattr__ at 0x7f25faabb510>, '__repr__': <cyfunction TemplateObjectGetter.__repr__ at 0x7f25faabb5e0>, '__dict__': <attribute '__dict__' of 'TemplateObjectGetter' objects>, '__weakref__': <attribute '__weakref__' of 'TemplateObjectGetter' objects>, '__doc__': None})"


class unicode_(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def removeprefix(self, *args, **kwargs): # real signature unknown
        """
        Return a str with the given prefix string removed if present.
        
        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """
        pass

    def removesuffix(self, *args, **kwargs): # real signature unknown
        """
        Return a str with the given suffix string removed if present.
        
        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the substrings in the string, using sep as the separator string.
        
          sep
            The separator used to split the string.
        
            When set to None (the default value), will split on any whitespace
            character (including \n \r \t \f and spaces) and will discard
            empty strings from the result.
          maxsplit
            Maximum number of splits.
            -1 (the default value) means no limit.
        
        Splitting starts at the end of the string and works to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self): # real signature unknown; restored from __doc__
        """
        Return a list of the substrings in the string, using sep as the separator string.
        
          sep
            The separator used to split the string.
        
            When set to None (the default value), will split on any whitespace
            character (including \n \r \t \f and spaces) and will discard
            empty strings from the result.
          maxsplit
            Maximum number of splits.
            -1 (the default value) means no limit.
        
        Splitting starts at the front of the string and works to the end.
        
        Note, str.split() is mainly useful for data that has been intentionally
        delimited.  With natural text that includes punctuation, consider using
        the regular expression module.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class _TemplateBreak(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class _TemplateContinue(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

basestring_ = (
    bytes,
    str,
)

in_re = None # (!) real value is "re.compile('\\\\s+in\\\\s+')"

lead_whitespace_re = None # (!) real value is "re.compile('^[\\\\t ]*\\\\n')"

single_statements = [
    'else',
    'endif',
    'endfor',
    'enddef',
    'continue',
    'break',
]

statement_re = None # (!) real value is "re.compile('^(?:if |elif |for |def |inherit |default |py:)')"

trail_whitespace_re = None # (!) real value is "re.compile('\\\\n\\\\r?[\\\\t ]*$')"

var_re = None # (!) real value is "re.compile('^[a-z_][a-z0-9_]*$', re.IGNORECASE)"

__all__ = [
    'TemplateError',
    'Template',
    'sub',
    'bunch',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacea10>'

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Tempita._tempita', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacea10>, origin='/usr/lib/python3.11/site-packages/Cython/Tempita/_tempita.cpython-311-x86_64-linux-gnu.so')"

__test__ = {
    'lex (line 537)': "\n    Lex a string into chunks:\n\n        >>> lex('hey')\n        ['hey']\n        >>> lex('hey {{you}}')\n        ['hey ', ('you', (1, 7))]\n        >>> lex('hey {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No }} to finish last expression at line 1 column 7\n        >>> lex('hey }}')\n        Traceback (most recent call last):\n            ...\n        TemplateError: }} outside expression at line 1 column 7\n        >>> lex('hey {{ {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: {{ inside expression at line 1 column 10\n\n    ",
    'parse (line 674)': '\n    Parses a string into a kind of AST\n\n        >>> parse(\'{{x}}\')\n        [(\'expr\', (1, 3), \'x\')]\n        >>> parse(\'foo\')\n        [\'foo\']\n        >>> parse(\'{{if x}}test{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'test\']))]\n        >>> parse(\'series->{{for x in y}}x={{x}}{{endfor}}\')\n        [\'series->\', (\'for\', (1, 11), (\'x\',), \'y\', [\'x=\', (\'expr\', (1, 27), \'x\')])]\n        >>> parse(\'{{for x, y in z:}}{{continue}}{{endfor}}\')\n        [(\'for\', (1, 3), (\'x\', \'y\'), \'z\', [(\'continue\', (1, 21))])]\n        >>> parse(\'{{py:x=1}}\')\n        [(\'py\', (1, 3), \'x=1\')]\n        >>> parse(\'{{if x}}a{{elif y}}b{{else}}c{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'a\']), (\'elif\', (1, 12), \'y\', [\'b\']), (\'else\', (1, 23), None, [\'c\']))]\n\n    Some exceptions::\n\n        >>> parse(\'{{continue}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: continue outside of for loop at line 1 column 3\n        >>> parse(\'{{if x}}foo\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No {{endif}} at line 1 column 3\n        >>> parse(\'{{else}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: else outside of an if block at line 1 column 3\n        >>> parse(\'{{if x}}{{for x in y}}{{endif}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Unexpected endif at line 1 column 25\n        >>> parse(\'{{if}}{{endif}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: if with no expression at line 1 column 3\n        >>> parse(\'{{for x y}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Bad for (no "in") in \'x y\' at line 1 column 3\n        >>> parse(\'{{py:x=1\\ny=2}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Multi-line py blocks must start with a newline at line 1 column 3\n    ',
    'trim_lex (line 606)': "\n    Takes a lexed set of tokens, and removes whitespace when there is\n    a directive on a line by itself:\n\n       >>> tokens = lex('{{if x}}\\nx\\n{{endif}}\\ny', trim_whitespace=False)\n       >>> tokens\n       [('if x', (1, 3)), '\\nx\\n', ('endif', (3, 3)), '\\ny']\n       >>> trim_lex(tokens)\n       [('if x', (1, 3)), 'x\\n', ('endif', (3, 3)), 'y']\n    ",
}

