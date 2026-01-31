# encoding: utf-8
# module rapidfuzz.distance._initialize_cpp
# from /app/lib/python3.11/site-packages/rapidfuzz/distance/_initialize_cpp.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def __pyx_unpickle_Editop(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Opcode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ScoreAlignment(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Editop(object):
    """
    Tuple like object describing an edit operation.
        It is in the form (tag, src_pos, dest_pos)
    
        The tags are strings, with these meanings:
    
        +-----------+---------------------------------------------------+
        | tag       | explanation                                       |
        +===========+===================================================+
        | 'replace' | src[src_pos] should be replaced by dest[dest_pos] |
        +-----------+---------------------------------------------------+
        | 'delete'  | src[src_pos] should be deleted                    |
        +-----------+---------------------------------------------------+
        | 'insert'  | dest[dest_pos] should be inserted at src[src_pos] |
        +-----------+---------------------------------------------------+
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dest_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Editops(object):
    """ List like object of Editops describing how to turn s1 into s2. """
    def apply(self, *args, **kwargs): # real signature unknown
        """
        apply editops to source_string
        
                Parameters
                ----------
                source_string : str | bytes
                    string to apply editops to
                destination_string : str | bytes
                    string to use for replacements / insertions into source_string
        
                Returns
                -------
                mod_string : str
                    modified source_string
        """
        pass

    def as_list(self, *args, **kwargs): # real signature unknown
        """
        Convert Editops to a list of tuples.
        
                This is the equivalent of ``[x for x in editops]``
        """
        pass

    def as_matching_blocks(self, *args, **kwargs): # real signature unknown
        """
        Convert to matching blocks
        
                Returns
                -------
                matching blocks : list[MatchingBlock]
                    Editops converted to matching blocks
        """
        pass

    def as_opcodes(self, *args, **kwargs): # real signature unknown
        """
        Convert to Opcodes
        
                Returns
                -------
                opcodes : Opcodes
                    Editops converted to Opcodes
        """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ performs copy of Editops """
        pass

    @classmethod
    def from_opcodes(cls, *args, **kwargs): # real signature unknown
        """
        Create Editops from Opcodes
        
                Parameters
                ----------
                opcodes : Opcodes
                    opcodes to convert to editops
        
                Returns
                -------
                editops : Editops
                    Opcodes converted to Editops
        """
        pass

    def inverse(self): # real signature unknown; restored from __doc__
        """
        Invert Editops, so it describes how to transform the destination string to
                the source string.
        
                Returns
                -------
                editops : Editops
                    inverted Editops
        
                Examples
                --------
                >>> from rapidfuzz.distance import Levenshtein
                >>> Levenshtein.editops('spam', 'park')
                [Editop(tag=delete, src_pos=0, dest_pos=0),
                 Editop(tag=replace, src_pos=3, dest_pos=2),
                 Editop(tag=insert, src_pos=4, dest_pos=3)]
        
                >>> Levenshtein.editops('spam', 'park').inverse()
                [Editop(tag=insert, src_pos=0, dest_pos=0),
                 Editop(tag=replace, src_pos=2, dest_pos=3),
                 Editop(tag=delete, src_pos=3, dest_pos=4)]
        """
        pass

    def remove_subsequence(self, *args, **kwargs): # real signature unknown
        """
        remove a subsequence
        
                Parameters
                ----------
                subsequence : Editops
                    subsequence to remove (has to be a subset of editops)
        
                Returns
                -------
                sequence : Editops
                    a copy of the editops without the subsequence
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dest_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class MatchingBlock(object):
    """ Triple describing matching subsequences """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Opcode(object):
    """
    Tuple like object describing an edit operation.
        It is in the form (tag, src_start, src_end, dest_start, dest_end)
    
        The tags are strings, with these meanings:
    
        +-----------+-----------------------------------------------------+
        | tag       | explanation                                         |
        +===========+=====================================================+
        | 'replace' | src[src_start:src_end] should be                    |
        |           | replaced by dest[dest_start:dest_end]               |
        +-----------+-----------------------------------------------------+
        | 'delete'  | src[src_start:src_end] should be deleted.           |
        |           | Note that dest_start==dest_end in this case.        |
        +-----------+-----------------------------------------------------+
        | 'insert'  | dest[dest_start:dest_end] should be inserted        |
        |           | at src[src_start:src_start].                        |
        |           | Note that src_start==src_end in this case.          |
        +-----------+-----------------------------------------------------+
        | 'equal'   | src[src_start:src_end] == dest[dest_start:dest_end] |
        +-----------+-----------------------------------------------------+
    
        Note
        ----
        Opcode is compatible with the tuples returned by difflib's SequenceMatcher to make them
        interoperable
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dest_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dest_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Opcodes(object):
    """
    List like object of Opcodes describing how to turn s1 into s2.
        The first Opcode has src_start == dest_start == 0, and remaining tuples
        have src_start == the src_end from the tuple preceding it,
        and likewise for dest_start == the previous dest_end.
    """
    def apply(self, *args, **kwargs): # real signature unknown
        """
        apply opcodes to source_string
        
                Parameters
                ----------
                source_string : str | bytes
                    string to apply opcodes to
                destination_string : str | bytes
                    string to use for replacements / insertions into source_string
        
                Returns
                -------
                mod_string : str
                    modified source_string
        """
        pass

    def as_editops(self, *args, **kwargs): # real signature unknown
        """
        Convert to Editops
        
                Returns
                -------
                editops : Editops
                    Opcodes converted to Editops
        """
        pass

    def as_list(self, *args, **kwargs): # real signature unknown
        """
        Convert Opcodes to a list of tuples, which is compatible
                with the opcodes of difflibs SequenceMatcher.
        
                This is the equivalent of ``[x for x in opcodes]``
        """
        pass

    def as_matching_blocks(self, *args, **kwargs): # real signature unknown
        """
        Convert to matching blocks
        
                Returns
                -------
                matching blocks : list[MatchingBlock]
                    Opcodes converted to matching blocks
        """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ performs copy of Opcodes """
        pass

    @classmethod
    def from_editops(cls, *args, **kwargs): # real signature unknown
        """
        Create Opcodes from Editops
        
                Parameters
                ----------
                editops : Editops
                    editops to convert to opcodes
        
                Returns
                -------
                opcodes : Opcodes
                    Editops converted to Opcodes
        """
        pass

    def inverse(self): # real signature unknown; restored from __doc__
        """
        Invert Opcodes, so it describes how to transform the destination string to
                the source string.
        
                Returns
                -------
                opcodes : Opcodes
                    inverted Opcodes
        
                Examples
                --------
                >>> from rapidfuzz.distance import Levenshtein
                >>> Levenshtein.opcodes('spam', 'park')
                [Opcode(tag=delete, src_start=0, src_end=1, dest_start=0, dest_end=0),
                 Opcode(tag=equal, src_start=1, src_end=3, dest_start=0, dest_end=2),
                 Opcode(tag=replace, src_start=3, src_end=4, dest_start=2, dest_end=3),
                 Opcode(tag=insert, src_start=4, src_end=4, dest_start=3, dest_end=4)]
        
                >>> Levenshtein.opcodes('spam', 'park').inverse()
                [Opcode(tag=insert, src_start=0, src_end=0, dest_start=0, dest_end=1),
                 Opcode(tag=equal, src_start=0, src_end=2, dest_start=1, dest_end=3),
                 Opcode(tag=replace, src_start=2, src_end=3, dest_start=3, dest_end=4),
                 Opcode(tag=delete, src_start=3, src_end=4, dest_start=4, dest_end=4)]
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dest_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class ScoreAlignment(object):
    """
    Tuple like object describing the position of the compared strings in
        src and dest.
    
        It indicates that the score has been calculated between
        src[src_start:src_end] and dest[dest_start:dest_end]
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dest_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dest_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    score = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8b6690>'

__spec__ = None # (!) real value is "ModuleSpec(name='rapidfuzz.distance._initialize_cpp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8b6690>, origin='/app/lib/python3.11/site-packages/rapidfuzz/distance/_initialize_cpp.cpython-311-x86_64-linux-gnu.so')"

__test__ = {
    'Editops.inverse (line 432)': "\n        Invert Editops, so it describes how to transform the destination string to\n        the source string.\n\n        Returns\n        -------\n        editops : Editops\n            inverted Editops\n\n        Examples\n        --------\n        >>> from rapidfuzz.distance import Levenshtein\n        >>> Levenshtein.editops('spam', 'park')\n        [Editop(tag=delete, src_pos=0, dest_pos=0),\n         Editop(tag=replace, src_pos=3, dest_pos=2),\n         Editop(tag=insert, src_pos=4, dest_pos=3)]\n\n        >>> Levenshtein.editops('spam', 'park').inverse()\n        [Editop(tag=insert, src_pos=0, dest_pos=0),\n         Editop(tag=replace, src_pos=2, dest_pos=3),\n         Editop(tag=delete, src_pos=3, dest_pos=4)]\n        ",
    'Opcodes.inverse (line 733)': "\n        Invert Opcodes, so it describes how to transform the destination string to\n        the source string.\n\n        Returns\n        -------\n        opcodes : Opcodes\n            inverted Opcodes\n\n        Examples\n        --------\n        >>> from rapidfuzz.distance import Levenshtein\n        >>> Levenshtein.opcodes('spam', 'park')\n        [Opcode(tag=delete, src_start=0, src_end=1, dest_start=0, dest_end=0),\n         Opcode(tag=equal, src_start=1, src_end=3, dest_start=0, dest_end=2),\n         Opcode(tag=replace, src_start=3, src_end=4, dest_start=2, dest_end=3),\n         Opcode(tag=insert, src_start=4, src_end=4, dest_start=3, dest_end=4)]\n\n        >>> Levenshtein.opcodes('spam', 'park').inverse()\n        [Opcode(tag=insert, src_start=0, src_end=0, dest_start=0, dest_end=1),\n         Opcode(tag=equal, src_start=0, src_end=2, dest_start=1, dest_end=3),\n         Opcode(tag=replace, src_start=2, src_end=3, dest_start=3, dest_end=4),\n         Opcode(tag=delete, src_start=3, src_end=4, dest_start=4, dest_end=4)]\n        ",
}

