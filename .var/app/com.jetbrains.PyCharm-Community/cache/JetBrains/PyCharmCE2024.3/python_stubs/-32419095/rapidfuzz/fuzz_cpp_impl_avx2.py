# encoding: utf-8
# module rapidfuzz.fuzz_cpp_impl_avx2
# from /app/lib/python3.11/site-packages/rapidfuzz/fuzz_cpp_impl_avx2.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from array import array

from rapidfuzz.distance._initialize_cpp import ScoreAlignment

from rapidfuzz.utils_cpp import default_process


# functions

def partial_ratio(this_is_a_test, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Searches for the optimal alignment of the shorter string in the
        longer string and returns the fuzz.ratio for this alignment.
    
        Parameters
        ----------
        s1 : str | bytes
            First string to compare.
        s2 : str | bytes
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        Depending on the length of the needle (shorter string) different
        implementations are used to improve the performance.
    
        short needle (length ≤ 64):
            When using a short needle length the fuzz.ratio is calculated for all
            alignments that could result in an optimal alignment. It is
            guaranteed to find the optimal alignment. For short needles this is very
            fast, since for them fuzz.ratio runs in ``O(N)`` time. This results in a worst
            case performance of ``O(NM)``.
    
        .. image:: img/partial_ratio_short_needle.svg
    
        long needle (length > 64):
            For long needles a similar implementation to FuzzyWuzzy is used.
            This implementation only considers alignments which start at one
            of the longest common substrings. This results in a worst case performance
            of ``O(N[N/64]M)``. However usually most of the alignments can be skipped.
            The following Python code shows the concept:
    
            .. code-block:: python
    
                blocks = SequenceMatcher(None, needle, longer, False).get_matching_blocks()
                score = 0
                for block in blocks:
                    long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
                    long_end = long_start + len(shorter)
                    long_substr = longer[long_start:long_end]
                    score = max(score, fuzz.ratio(needle, long_substr))
    
            This is a lot faster than checking all possible alignments. However it
            only finds one of the best alignments and not necessarily the optimal one.
    
        .. image:: img/partial_ratio_long_needle.svg
    
        Examples
        --------
        >>> fuzz.partial_ratio("this is a test", "this is a test!")
        100.0
    """
    pass

def partial_ratio_alignment(s1, s2): # real signature unknown; restored from __doc__
    """
    Searches for the optimal alignment of the shorter string in the
        longer string and returns the fuzz.ratio and the corresponding
        alignment.
    
        Parameters
        ----------
        s1 : str | bytes
            First string to compare.
        s2 : str | bytes
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff None is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        alignment : ScoreAlignment, optional
            alignment between s1 and s2 with the score as a float between 0 and 100
    
        Examples
        --------
        >>> s1 = "a certain string"
        >>> s2 = "cetain"
        >>> res = fuzz.partial_ratio_alignment(s1, s2)
        >>> res
        ScoreAlignment(score=83.33333333333334, src_start=2, src_end=8, dest_start=0, dest_end=6)
    
        Using the alignment information it is possible to calculate the same fuzz.ratio
    
        >>> fuzz.ratio(s1[res.src_start:res.src_end], s2[res.dest_start:res.dest_end])
        83.33333333333334
    """
    pass

def partial_token_ratio(*args, **kwargs): # real signature unknown
    """
    Helper method that returns the maximum of fuzz.partial_token_set_ratio and
        fuzz.partial_token_sort_ratio (faster than manually executing the two functions)
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/partial_token_ratio.svg
    """
    pass

def partial_token_set_ratio(*args, **kwargs): # real signature unknown
    """
    Compares the words in the strings based on unique and common words between them
        using fuzz.partial_ratio
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/partial_token_set_ratio.svg
    """
    pass

def partial_token_sort_ratio(*args, **kwargs): # real signature unknown
    """
    sorts the words in the strings and calculates the fuzz.partial_ratio between them
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/partial_token_sort_ratio.svg
    """
    pass

def QRatio(this_is_a_test, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Calculates a quick ratio between two strings using fuzz.ratio.
        The only difference to fuzz.ratio is, that this preprocesses
        the strings by default.
    
        Parameters
        ----------
        s1 : str | bytes
            First string to compare.
        s2 : str | bytes
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Examples
        --------
        >>> fuzz.QRatio("this is a test", "THIS is a test!")
        100.0
    """
    pass

def ratio(this_is_a_test, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Calculates the normalized Indel distance.
    
        Parameters
        ----------
        s1 : str | bytes
            First string to compare.
        s2 : str | bytes
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        See Also
        --------
        rapidfuzz.string_metric.normalized_levenshtein : Normalized levenshtein distance
    
        Notes
        -----
        .. image:: img/ratio.svg
    
        Examples
        --------
        >>> fuzz.ratio("this is a test", "this is a test!")
        96.55171966552734
    """
    pass

def token_ratio(*args, **kwargs): # real signature unknown
    """
    Helper method that returns the maximum of fuzz.token_set_ratio and fuzz.token_sort_ratio
        (faster than manually executing the two functions)
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/token_ratio.svg
    """
    pass

def token_set_ratio(fuzzy_was_a_bear, fuzzy_fuzzy_was_a_bear): # real signature unknown; restored from __doc__
    """
    Compares the words in the strings based on unique and common words between them
        using fuzz.ratio
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/token_set_ratio.svg
    
        Examples
        --------
        >>> fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        83.8709716796875
        >>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        100.0
    """
    pass

def token_sort_ratio(fuzzy_wuzzy_was_a_bear, wuzzy_fuzzy_was_a_bear): # real signature unknown; restored from __doc__
    """
    Sorts the words in the strings and calculates the fuzz.ratio between them
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/token_sort_ratio.svg
    
        Examples
        --------
        >>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        100.0
    """
    pass

def WRatio(*args, **kwargs): # real signature unknown
    """
    Calculates a weighted ratio based on the other ratio algorithms
    
        Parameters
        ----------
        s1 : str
            First string to compare.
        s2 : str
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is ``utils.default_process``.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 100.
            For ratio < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 100
    
        Notes
        -----
        .. image:: img/WRatio.svg
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8ee050>'

__spec__ = None # (!) real value is "ModuleSpec(name='rapidfuzz.fuzz_cpp_impl_avx2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8ee050>, origin='/app/lib/python3.11/site-packages/rapidfuzz/fuzz_cpp_impl_avx2.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

