# encoding: utf-8
# module rapidfuzz.process_cpp_impl
# from /app/lib/python3.11/site-packages/rapidfuzz/process_cpp_impl.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import heapq as heapq # /usr/lib/python3.11/heapq.py
from array import array

from rapidfuzz.fuzz_cpp_impl_avx2 import WRatio, ratio

from rapidfuzz.utils_cpp import default_process

import enum as __enum


# Variables with simple values

FLOAT32 = 1
FLOAT64 = 2

INT16 = 4
INT32 = 5
INT64 = 6
INT8 = 3

UINT16 = 8
UINT32 = 9
UINT64 = 10
UINT8 = 7

# functions

def cdist(*args, **kwargs): # real signature unknown
    pass

def extract(*args, **kwargs): # real signature unknown
    """
    Find the best matches in a list of choices. The list is sorted by the similarity.
        When multiple choices have the same similarity, they are sorted by their index
    
        Parameters
        ----------
        query : Sequence[Hashable]
            string we want to find
        choices : Collection[Sequence[Hashable]] | Mapping[Sequence[Hashable]]
            list of all strings the query should be compared with or dict with a mapping
            {<result>: <string to compare>}
        scorer : Callable, optional
            Optional callable that is used to calculate the matching score between
            the query and each choice. This can be any of the scorers included in RapidFuzz
            (both scorers that calculate the edit distance or the normalized edit distance), or
            a custom function, which returns a normalized edit distance.
            fuzz.WRatio is used by default.
        processor : Callable, optional
            Optional callable that reformats the strings.
            utils.default_process is used by default, which lowercases the strings and trims whitespace
        limit : int
            maximum amount of results to return
        score_cutoff : Any, optional
            Optional argument for a score threshold. When an edit distance is used this represents the maximum
            edit distance and matches with a `distance <= score_cutoff` are ignored. When a
            normalized edit distance is used this represents the minimal similarity
            and matches with a `similarity >= score_cutoff` are ignored. Default is None, which deactivates this behaviour.
        score_hint : Any, optional
            Optional argument for an expected score to be passed to the scorer.
            This is used to select a faster implementation. Default is None,
            which deactivates this behaviour.
        **kwargs : Any, optional
            any other named parameters are passed to the scorer. This can be used to pass
            e.g. weights to string_metric.levenshtein
    
        Returns
        -------
        List[Tuple[Sequence[Hashable], Any, Any]]
            The return type is always a List of Tuples with 3 elements. However the values stored in the
            tuple depend on the types of the input arguments.
    
            * The first element is always the `choice`, which is the value that's compared to the query.
    
            * The second value represents the similarity calculated by the scorer. This can be:
    
              * An edit distance (distance is 0 for a perfect match and > 0 for non perfect matches).
                In this case only choices which have a `distance <= max` are returned.
                An example of a scorer with this behavior is `string_metric.levenshtein`.
              * A normalized edit distance (similarity is a score between 0 and 100, with 100 being a perfect match).
                In this case only choices which have a `similarity >= score_cutoff` are returned.
                An example of a scorer with this behavior is `string_metric.normalized_levenshtein`.
    
              Note, that for all scorers, which are not provided by RapidFuzz, only normalized edit distances are supported.
    
            * The third parameter depends on the type of the `choices` argument it is:
    
              * The `index of choice` when choices is a simple iterable like a list
              * The `key of choice` when choices is a mapping like a dict, or a pandas Series
    
            The list is sorted by `score_cutoff` or `max` depending on the scorer used. The first element in the list
            has the `highest similarity`/`smallest distance`.
    """
    pass

def extractOne(abcd, abce=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Find the best match in a list of choices. When multiple elements have the same similarity,
        the first element is returned.
    
        Parameters
        ----------
        query : Sequence[Hashable]
            string we want to find
        choices : Iterable[Sequence[Hashable]] | Mapping[Sequence[Hashable]]
            list of all strings the query should be compared with or dict with a mapping
            {<result>: <string to compare>}
        scorer : Callable, optional
            Optional callable that is used to calculate the matching score between
            the query and each choice. This can be any of the scorers included in RapidFuzz
            (both scorers that calculate the edit distance or the normalized edit distance), or
            a custom function, which returns a normalized edit distance.
            fuzz.WRatio is used by default.
        processor : Callable, optional
            Optional callable that reformats the strings.
            utils.default_process is used by default, which lowercases the strings and trims whitespace
        score_cutoff : Any, optional
            Optional argument for a score threshold. When an edit distance is used this represents the maximum
            edit distance and matches with a `distance <= score_cutoff` are ignored. When a
            normalized edit distance is used this represents the minimal similarity
            and matches with a `similarity >= score_cutoff` are ignored. Default is None, which deactivates this behaviour.
        score_hint : Any, optional
            Optional argument for an expected score to be passed to the scorer.
            This is used to select a faster implementation. Default is None,
            which deactivates this behaviour.
        **kwargs : Any, optional
            any other named parameters are passed to the scorer. This can be used to pass
            e.g. weights to string_metric.levenshtein
    
        Returns
        -------
        Tuple[Sequence[Hashable], Any, Any]
            Returns the best match in form of a Tuple with 3 elements. The values stored in the
            tuple depend on the types of the input arguments.
    
            * The first element is always the `choice`, which is the value that's compared to the query.
    
            * The second value represents the similarity calculated by the scorer. This can be:
    
              * An edit distance (distance is 0 for a perfect match and > 0 for non perfect matches).
                In this case only choices which have a `distance <= score_cutoff` are returned.
                An example of a scorer with this behavior is `string_metric.levenshtein`.
              * A normalized edit distance (similarity is a score between 0 and 100, with 100 being a perfect match).
                In this case only choices which have a `similarity >= score_cutoff` are returned.
                An example of a scorer with this behavior is `string_metric.normalized_levenshtein`.
    
              Note, that for all scorers, which are not provided by RapidFuzz, only normalized edit distances are supported.
    
            * The third parameter depends on the type of the `choices` argument it is:
    
              * The `index of choice` when choices is a simple iterable like a list
              * The `key of choice` when choices is a mapping like a dict, or a pandas Series
    
        None
            When no choice has a `similarity >= score_cutoff`/`distance <= score_cutoff` None is returned
    
        Examples
        --------
    
        >>> from rapidfuzz.process import extractOne
        >>> from rapidfuzz.string_metric import levenshtein, normalized_levenshtein
        >>> from rapidfuzz.fuzz import ratio
    
        extractOne can be used with normalized edit distances.
    
        >>> extractOne("abcd", ["abce"], scorer=ratio)
        ("abcd", 75.0, 1)
        >>> extractOne("abcd", ["abce"], scorer=normalized_levenshtein)
        ("abcd", 75.0, 1)
    
        extractOne can be used with edit distances as well.
    
        >>> extractOne("abcd", ["abce"], scorer=levenshtein)
        ("abce", 1, 0)
    
        additional settings of the scorer can be passed as keyword arguments to extractOne
    
        >>> extractOne("abcd", ["abce"], scorer=levenshtein, weights=(1,1,2))
        ("abcde", 2, 1)
    
        when a mapping is used for the choices the key of the choice is returned instead of the List index
    
        >>> extractOne("abcd", {"key": "abce"}, scorer=ratio)
        ("abcd", 75.0, "key")
    
        By default each string is preprocessed using `utils.default_process`, which lowercases the strings,
        replaces non alphanumeric characters with whitespaces and trims whitespaces from start and end of them.
        This behavior can be changed by passing a custom function, or None to disable the behavior. Preprocessing
        can take a significant part of the runtime, so it makes sense to disable it, when it is not required.
    
    
        >>> extractOne("abcd", ["abdD"], scorer=ratio)
        ("abcD", 100.0, 0)
        >>> extractOne("abcd", ["abdD"], scorer=ratio, processor=None)
        ("abcD", 75.0, 0)
        >>> extractOne("abcd", ["abdD"], scorer=ratio, processor=lambda s: s.upper())
        ("abcD", 100.0, 0)
    
        When only results with a similarity above a certain threshold are relevant, the parameter score_cutoff can be
        used to filter out results with a lower similarity. This threshold is used by some of the scorers to exit early,
        when they are sure, that the similarity is below the threshold.
        For normalized edit distances all results with a similarity below score_cutoff are filtered out
    
        >>> extractOne("abcd", ["abce"], scorer=ratio)
        ("abce", 75.0, 0)
        >>> extractOne("abcd", ["abce"], scorer=ratio, score_cutoff=80)
        None
    
        For edit distances all results with an edit distance above the score_cutoff are filtered out
    
        >>> extractOne("abcd", ["abce"], scorer=levenshtein, weights=(1,1,2))
        ("abce", 2, 0)
        >>> extractOne("abcd", ["abce"], scorer=levenshtein, weights=(1,1,2), score_cutoff=1)
        None
    """
    pass

def extract_iter(*args, **kwargs): # real signature unknown
    """
    Find the best match in a list of choices
    
        Parameters
        ----------
        query : Sequence[Hashable]
            string we want to find
        choices : Iterable[Sequence[Hashable]] | Mapping[Sequence[Hashable]]
            list of all strings the query should be compared with or dict with a mapping
            {<result>: <string to compare>}
        scorer : Callable, optional
            Optional callable that is used to calculate the matching score between
            the query and each choice. This can be any of the scorers included in RapidFuzz
            (both scorers that calculate the edit distance or the normalized edit distance), or
            a custom function, which returns a normalized edit distance.
            fuzz.WRatio is used by default.
        processor : Callable, optional
            Optional callable that reformats the strings.
            utils.default_process is used by default, which lowercases the strings and trims whitespace
        score_cutoff : Any, optional
            Optional argument for a score threshold. When an edit distance is used this represents the maximum
            edit distance and matches with a `distance <= score_cutoff` are ignored. When a
            normalized edit distance is used this represents the minimal similarity
            and matches with a `similarity >= score_cutoff` are ignored. Default is None, which deactivates this behaviour.
        score_hint : Any, optional
            Optional argument for an expected score to be passed to the scorer.
            This is used to select a faster implementation. Default is None,
            which deactivates this behaviour.
        **kwargs : Any, optional
            any other named parameters are passed to the scorer. This can be used to pass
            e.g. weights to string_metric.levenshtein
    
        Yields
        -------
        Tuple[Sequence[Hashable], Any, Any]
            Yields similarity between the query and each choice in form of a Tuple with 3 elements.
            The values stored in the tuple depend on the types of the input arguments.
    
            * The first element is always the current `choice`, which is the value that's compared to the query.
    
            * The second value represents the similarity calculated by the scorer. This can be:
    
              * An edit distance (distance is 0 for a perfect match and > 0 for non perfect matches).
                In this case only choices which have a `distance <= max` are yielded.
                An example of a scorer with this behavior is `string_metric.levenshtein`.
              * A normalized edit distance (similarity is a score between 0 and 100, with 100 being a perfect match).
                In this case only choices which have a `similarity >= score_cutoff` are yielded.
                An example of a scorer with this behavior is `string_metric.normalized_levenshtein`.
    
              Note, that for all scorers, which are not provided by RapidFuzz, only normalized edit distances are supported.
    
            * The third parameter depends on the type of the `choices` argument it is:
    
              * The `index of choice` when choices is a simple iterable like a list
              * The `key of choice` when choices is a mapping like a dict, or a pandas Series
    """
    pass

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Matrix(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class MatrixType(__enum.IntEnum):
    # no doc
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def _value_repr_(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    FLOAT32 = 1
    FLOAT64 = 2
    INT16 = 4
    INT32 = 5
    INT64 = 6
    INT8 = 3
    UINT16 = 8
    UINT32 = 9
    UINT64 = 10
    UINT8 = 7
    UNDEFINED = 0
    _member_map_ = {
        'FLOAT32': 1,
        'FLOAT64': 2,
        'INT16': 4,
        'INT32': 5,
        'INT64': 6,
        'INT8': 3,
        'UINT16': 8,
        'UINT32': 9,
        'UINT64': 10,
        'UINT8': 7,
        'UNDEFINED': 0,
    }
    _member_names_ = [
        'UNDEFINED',
        'FLOAT32',
        'FLOAT64',
        'INT8',
        'INT16',
        'INT32',
        'INT64',
        'UINT8',
        'UINT16',
        'UINT32',
        'UINT64',
    ]
    _member_type_ = int
    _unhashable_values_ = []
    _use_args_ = True
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa905390>'

__spec__ = None # (!) real value is "ModuleSpec(name='rapidfuzz.process_cpp_impl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa905390>, origin='/app/lib/python3.11/site-packages/rapidfuzz/process_cpp_impl.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

