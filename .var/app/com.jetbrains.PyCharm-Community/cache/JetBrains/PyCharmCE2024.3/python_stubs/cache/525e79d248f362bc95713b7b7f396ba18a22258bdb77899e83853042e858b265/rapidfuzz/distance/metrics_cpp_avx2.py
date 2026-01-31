# encoding: utf-8
# module rapidfuzz.distance.metrics_cpp_avx2
# from /app/lib/python3.11/site-packages/rapidfuzz/distance/metrics_cpp_avx2.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from array import array


# functions

def damerau_levenshtein_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the Damerau-Levenshtein distance.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Examples
        --------
        Find the Damerau-Levenshtein distance between two strings:
    
        >>> from rapidfuzz.distance import DamerauLevenshtein
        >>> DamerauLevenshtein.distance("CA", "ABC")
        2
    """
    pass

def damerau_levenshtein_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized Damerau-Levenshtein similarity in the range [1, 0].
    
        This is calculated as ``distance / max(len1, len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def damerau_levenshtein_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized Damerau-Levenshtein similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def damerau_levenshtein_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the Damerau-Levenshtein similarity in the range [max, 0].
    
        This is calculated as ``max(len1, len2) - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        similarity : int
            similarity between s1 and s2
    """
    pass

def hamming_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the Hamming distance between two strings.
        The hamming distance is defined as the number of positions
        where the two strings differ. It describes the minimum
        amount of substitutions required to transform s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int or None, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Raises
        ------
        ValueError
            If s1 and s2 have a different length
    """
    pass

def hamming_editops(*args, **kwargs): # real signature unknown
    """
    Return Editops describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        editops : Editops
            edit operations required to turn s1 into s2
    """
    pass

def hamming_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized Hamming similarity in the range [1, 0].
    
        This is calculated as ``distance / (len1 + len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    
        Raises
        ------
        ValueError
            If s1 and s2 have a different length
    """
    pass

def hamming_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized Hamming similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    
        Raises
        ------
        ValueError
            If s1 and s2 have a different length
    """
    pass

def hamming_opcodes(*args, **kwargs): # real signature unknown
    """
    Return Opcodes describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        opcodes : Opcodes
            edit operations required to turn s1 into s2
    """
    pass

def hamming_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the Hamming similarity between two strings.
    
        This is calculated as ``len1 - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Raises
        ------
        ValueError
            If s1 and s2 have a different length
    """
    pass

def indel_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the minimum number of insertions and deletions
        required to change one sequence into the other. This is equivalent to the
        Levenshtein distance with a substitution weight of 2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Examples
        --------
        Find the Indel distance between two strings:
    
        >>> from rapidfuzz.distance import Indel
        >>> Indel.distance("lewenstein", "levenshtein")
        3
    
        Setting a maximum distance allows the implementation to select
        a more efficient implementation:
    
        >>> Indel.distance("lewenstein", "levenshtein", score_cutoff=1)
        2
    """
    pass

def indel_editops(*args, **kwargs): # real signature unknown
    """
    Return Editops describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        editops : Editops
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [6]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [6] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import Indel
        >>> for tag, src_pos, dest_pos in Indel.editops("qabxcd", "abycdf"):
        ...    print(("%7s s1[%d] s2[%d]" % (tag, src_pos, dest_pos)))
         delete s1[0] s2[0]
         delete s1[3] s2[2]
         insert s1[4] s2[2]
         insert s1[6] s2[5]
    """
    pass

def indel_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized levenshtein similarity in the range [1, 0].
    
        This is calculated as ``distance / (len1 + len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def indel_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized indel similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    
        Examples
        --------
        Find the normalized Indel similarity between two strings:
    
        >>> from rapidfuzz.distance import Indel
        >>> Indel.normalized_similarity("lewenstein", "levenshtein")
        0.85714285714285
    
        Setting a score_cutoff allows the implementation to select
        a more efficient implementation:
    
        >>> Indel.normalized_similarity("lewenstein", "levenshtein", score_cutoff=0.9)
        0.0
    
        When a different processor is used s1 and s2 do not have to be strings
    
        >>> Indel.normalized_similarity(["lewenstein"], ["levenshtein"], processor=lambda s: s[0])
        0.8571428571428572
    """
    pass

def indel_opcodes(*args, **kwargs): # real signature unknown
    """
    Return Opcodes describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        opcodes : Opcodes
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [7]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [7] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import Indel
    
        >>> a = "qabxcd"
        >>> b = "abycdf"
        >>> for tag, i1, i2, j1, j2 in Indel.opcodes(a, b):
        ...    print(("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
        ...           (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
         delete a[0:1] (q) b[0:0] ()
          equal a[1:3] (ab) b[0:2] (ab)
         delete a[3:4] (x) b[2:2] ()
         insert a[4:4] () b[2:3] (y)
          equal a[4:6] (cd) b[3:5] (cd)
         insert a[6:6] () b[5:6] (f)
    """
    pass

def indel_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the Indel similarity in the range [max, 0].
    
        This is calculated as ``(len1 + len2) - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        similarity : int
            similarity between s1 and s2
    """
    pass

def jaro_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the jaro distance
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        distance : float
            distance between s1 and s2 as a float between 1.0 and 0.0
    """
    pass

def jaro_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the normalized jaro distance
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        normalized distance : float
            normalized distance between s1 and s2 as a float between 1.0 and 0.0
    """
    pass

def jaro_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the normalized jaro similarity
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        normalized similarity : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def jaro_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the jaro similarity
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def jaro_winkler_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the jaro winkler distance
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        prefix_weight : float, optional
            Weight used for the common prefix of the two strings.
            Has to be between 0 and 0.25. Default is 0.1.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        distance : float
            distance between s1 and s2 as a float between 1.0 and 0.0
    
        Raises
        ------
        ValueError
            If prefix_weight is invalid
    """
    pass

def jaro_winkler_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the normalized jaro winkler distance
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        prefix_weight : float, optional
            Weight used for the common prefix of the two strings.
            Has to be between 0 and 0.25. Default is 0.1.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        normalized distance : float
            normalized distance between s1 and s2 as a float between 1.0 and 0.0
    
        Raises
        ------
        ValueError
            If prefix_weight is invalid
    """
    pass

def jaro_winkler_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the normalized jaro winkler similarity
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        prefix_weight : float, optional
            Weight used for the common prefix of the two strings.
            Has to be between 0 and 0.25. Default is 0.1.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        normalized similarity : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    
        Raises
        ------
        ValueError
            If prefix_weight is invalid
    """
    pass

def jaro_winkler_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the jaro winkler similarity
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        prefix_weight : float, optional
            Weight used for the common prefix of the two strings.
            Has to be between 0 and 0.25. Default is 0.1.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For ratio < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
    
        Returns
        -------
        similarity : float
            similarity between s1 and s2 as a float between 0 and 1.0
    
        Raises
        ------
        ValueError
            If prefix_weight is invalid
    """
    pass

def lcs_seq_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the LCS distance in the range [0, max].
    
        This is calculated as ``max(len1, len2) - similarity``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Examples
        --------
        Find the LCS distance between two strings:
    
        >>> from rapidfuzz.distance import LCSseq
        >>> LCSseq.distance("lewenstein", "levenshtein")
        2
    
        Setting a maximum distance allows the implementation to select
        a more efficient implementation:
    
        >>> LCSseq.distance("lewenstein", "levenshtein", score_cutoff=1)
        2
    """
    pass

def lcs_seq_editops(*args, **kwargs): # real signature unknown
    """
    Return Editops describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        editops : Editops
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [6]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [6] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import LCSseq
        >>> for tag, src_pos, dest_pos in LCSseq.editops("qabxcd", "abycdf"):
        ...    print(("%7s s1[%d] s2[%d]" % (tag, src_pos, dest_pos)))
         delete s1[0] s2[0]
         delete s1[3] s2[2]
         insert s1[4] s2[2]
         insert s1[6] s2[5]
    """
    pass

def lcs_seq_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized LCS similarity in the range [1, 0].
    
        This is calculated as ``distance / max(len1, len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def lcs_seq_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized LCS similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    
        Examples
        --------
        Find the normalized LCS similarity between two strings:
    
        >>> from rapidfuzz.distance import LCSseq
        >>> LCSseq.normalized_similarity("lewenstein", "levenshtein")
        0.8181818181818181
    
        Setting a score_cutoff allows the implementation to select
        a more efficient implementation:
    
        >>> LCSseq.normalized_similarity("lewenstein", "levenshtein", score_cutoff=0.9)
        0.0
    
        When a different processor is used s1 and s2 do not have to be strings
    
        >>> LCSseq.normalized_similarity(["lewenstein"], ["levenshtein"], processor=lambda s: s[0])
        0.81818181818181
    """
    pass

def lcs_seq_opcodes(*args, **kwargs): # real signature unknown
    """
    Return Opcodes describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        opcodes : Opcodes
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [7]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [7] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import LCSseq
    
        >>> a = "qabxcd"
        >>> b = "abycdf"
        >>> for tag, i1, i2, j1, j2 in LCSseq.opcodes(a, b):
        ...    print(("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
        ...           (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
         delete a[0:1] (q) b[0:0] ()
          equal a[1:3] (ab) b[0:2] (ab)
         delete a[3:4] (x) b[2:2] ()
         insert a[4:4] () b[2:3] (y)
          equal a[4:6] (cd) b[3:5] (cd)
         insert a[6:6] () b[5:6] (f)
    """
    pass

def lcs_seq_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the length of the longest common subsequence
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        similarity : int
            similarity between s1 and s2
    """
    pass

def levenshtein_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the minimum number of insertions, deletions, and substitutions
        required to change one sequence into the other according to Levenshtein with custom
        costs for insertion, deletion and substitution
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        weights : Tuple[int, int, int] or None, optional
            The weights for the three operations in the form
            (insertion, deletion, substitution). Default is (1, 1, 1),
            which gives all three operations a weight of 1.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
        score_hint : int, optional
            Expected distance between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Raises
        ------
        ValueError
            If unsupported weights are provided a ValueError is thrown
    
        Examples
        --------
        Find the Levenshtein distance between two strings:
    
        >>> from rapidfuzz.distance import Levenshtein
        >>> Levenshtein.distance("lewenstein", "levenshtein")
        2
    
        Setting a maximum distance allows the implementation to select
        a more efficient implementation:
    
        >>> Levenshtein.distance("lewenstein", "levenshtein", score_cutoff=1)
        2
    
        It is possible to select different weights by passing a `weight`
        tuple.
    
        >>> Levenshtein.distance("lewenstein", "levenshtein", weights=(1,1,2))
        3
    """
    pass

def levenshtein_editops(*args, **kwargs): # real signature unknown
    """
    Return Editops describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_hint : int, optional
            Expected distance between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        editops : Editops
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [8]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [8] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import Levenshtein
        >>> for tag, src_pos, dest_pos in Levenshtein.editops("qabxcd", "abycdf"):
        ...    print(("%7s s1[%d] s2[%d]" % (tag, src_pos, dest_pos)))
         delete s1[1] s2[0]
        replace s1[3] s2[2]
         insert s1[6] s2[5]
    """
    pass

def levenshtein_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized levenshtein distance in the range [1, 0] using custom
        costs for insertion, deletion and substitution.
    
        This is calculated as ``distance / max``, where max is the maximal possible
        Levenshtein distance given the lengths of the sequences s1/s2 and the weights.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        weights : Tuple[int, int, int] or None, optional
            The weights for the three operations in the form
            (insertion, deletion, substitution). Default is (1, 1, 1),
            which gives all three operations a weight of 1.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is None,
            which deactivates this behaviour.
        score_hint : float, optional
            Expected normalized distance between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 1.0 and 0.0
    
        Raises
        ------
        ValueError
            If unsupported weights are provided a ValueError is thrown
    """
    pass

def levenshtein_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized levenshtein similarity in the range [0, 1] using custom
        costs for insertion, deletion and substitution.
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        weights : Tuple[int, int, int] or None, optional
            The weights for the three operations in the form
            (insertion, deletion, substitution). Default is (1, 1, 1),
            which gives all three operations a weight of 1.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is None,
            which deactivates this behaviour.
        score_hint : int, optional
            Expected normalized similarity between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    
        Raises
        ------
        ValueError
            If unsupported weights are provided a ValueError is thrown
    
        Examples
        --------
        Find the normalized Levenshtein similarity between two strings:
    
        >>> from rapidfuzz.distance import Levenshtein
        >>> Levenshtein.normalized_similarity("lewenstein", "levenshtein")
        0.81818181818181
    
        Setting a score_cutoff allows the implementation to select
        a more efficient implementation:
    
        >>> Levenshtein.normalized_similarity("lewenstein", "levenshtein", score_cutoff=0.85)
        0.0
    
        It is possible to select different weights by passing a `weight`
        tuple.
    
        >>> Levenshtein.normalized_similarity("lewenstein", "levenshtein", weights=(1,1,2))
        0.85714285714285
    
        When a different processor is used s1 and s2 do not have to be strings
    
        >>> Levenshtein.normalized_similarity(["lewenstein"], ["levenshtein"], processor=lambda s: s[0])
        0.81818181818181
    """
    pass

def levenshtein_opcodes(*args, **kwargs): # real signature unknown
    """
    Return Opcodes describing how to turn s1 into s2.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_hint : int, optional
            Expected distance between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        opcodes : Opcodes
            edit operations required to turn s1 into s2
    
        Notes
        -----
        The alignment is calculated using an algorithm of Heikki Hyyrö, which is
        described [9]_. It has a time complexity and memory usage of ``O([N/64] * M)``.
    
        References
        ----------
        .. [9] Hyyrö, Heikki. "A Note on Bit-Parallel Alignment Computation."
               Stringology (2004).
    
        Examples
        --------
        >>> from rapidfuzz.distance import Levenshtein
    
        >>> a = "qabxcd"
        >>> b = "abycdf"
        >>> for tag, i1, i2, j1, j2 in Levenshtein.opcodes("qabxcd", "abycdf"):
        ...    print(("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
        ...           (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
         delete a[0:1] (q) b[0:0] ()
          equal a[1:3] (ab) b[0:2] (ab)
        replace a[3:4] (x) b[2:3] (y)
          equal a[4:6] (cd) b[3:5] (cd)
         insert a[6:6] () b[5:6] (f)
    """
    pass

def levenshtein_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the levenshtein similarity in the range [max, 0] using custom
        costs for insertion, deletion and substitution.
    
        This is calculated as ``max - distance``, where max is the maximal possible
        Levenshtein distance given the lengths of the sequences s1/s2 and the weights.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        weights : Tuple[int, int, int] or None, optional
            The weights for the three operations in the form
            (insertion, deletion, substitution). Default is (1, 1, 1),
            which gives all three operations a weight of 1.
        processor : callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
        score_hint : int, optional
            Expected similarity between s1 and s2. This is used to select a
            faster implementation. Default is None, which deactivates this behaviour.
    
        Returns
        -------
        similarity : int
            similarity between s1 and s2
    
        Raises
        ------
        ValueError
            If unsupported weights are provided a ValueError is thrown
    """
    pass

def osa_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the optimal string alignment (OSA) distance.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    
        Examples
        --------
        Find the OSA distance between two strings:
    
        >>> from rapidfuzz.distance import OSA
        >>> OSA.distance("CA", "AC")
        2
        >>> OSA.distance("CA", "ABC")
        3
    """
    pass

def osa_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized optimal string alignment (OSA) similarity in the range [1, 0].
    
        This is calculated as ``distance / max(len1, len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def osa_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized optimal string alignment (OSA) similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def osa_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the optimal string alignment (OSA) similarity in the range [max, 0].
    
        This is calculated as ``max(len1, len2) - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        similarity : int
            similarity between s1 and s2
    """
    pass

def postfix_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the postfix distance between two strings.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int or None, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    """
    pass

def postfix_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized postfix similarity in the range [1, 0].
    
        This is calculated as ``distance / (len1 + len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def postfix_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized postfix similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def postfix_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the postfix similarity between two strings.
    
        This is calculated as ``len1 - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    """
    pass

def prefix_distance(*args, **kwargs): # real signature unknown
    """
    Calculates the Prefix distance between two strings.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int or None, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the distance is bigger than score_cutoff,
            score_cutoff + 1 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    """
    pass

def prefix_normalized_distance(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized prefix similarity in the range [1, 0].
    
        This is calculated as ``distance / (len1 + len2)``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_dist > score_cutoff 1.0 is returned instead. Default is 1.0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_dist : float
            normalized distance between s1 and s2 as a float between 0 and 1.0
    """
    pass

def prefix_normalized_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates a normalized prefix similarity in the range [0, 1].
    
        This is calculated as ``1 - normalized_distance``
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : float, optional
            Optional argument for a score threshold as a float between 0 and 1.0.
            For norm_sim < score_cutoff 0 is returned instead. Default is 0,
            which deactivates this behaviour.
    
        Returns
        -------
        norm_sim : float
            normalized similarity between s1 and s2 as a float between 0 and 1.0
    """
    pass

def prefix_similarity(*args, **kwargs): # real signature unknown
    """
    Calculates the prefix similarity between two strings.
    
        This is calculated as ``len1 - distance``.
    
        Parameters
        ----------
        s1 : Sequence[Hashable]
            First string to compare.
        s2 : Sequence[Hashable]
            Second string to compare.
        processor: callable, optional
            Optional callable that is used to preprocess the strings before
            comparing them. Default is None, which deactivates this behaviour.
        score_cutoff : int, optional
            Maximum distance between s1 and s2, that is
            considered as a result. If the similarity is smaller than score_cutoff,
            0 is returned instead. Default is None, which deactivates
            this behaviour.
    
        Returns
        -------
        distance : int
            distance between s1 and s2
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8b4410>'

__spec__ = None # (!) real value is "ModuleSpec(name='rapidfuzz.distance.metrics_cpp_avx2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fa8b4410>, origin='/app/lib/python3.11/site-packages/rapidfuzz/distance/metrics_cpp_avx2.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

