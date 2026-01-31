# encoding: utf-8
# module binascii
# from /usr/lib/python3.11/lib-dynload/binascii.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
""" Conversion between binary data and ASCII """
# no imports

# functions

def a2b_base64(*args, **kwargs): # real signature unknown
    """
    Decode a line of base64 data.
    
      strict_mode
        When set to True, bytes that are not part of the base64 standard are not allowed.
        The same applies to excess data after padding (= / ==).
    """
    pass

def a2b_hex(*args, **kwargs): # real signature unknown
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    This function is also available as "unhexlify()".
    """
    pass

def a2b_qp(*args, **kwargs): # real signature unknown
    """ Decode a string of qp-encoded data. """
    pass

def a2b_uu(*args, **kwargs): # real signature unknown
    """ Decode a line of uuencoded data. """
    pass

def b2a_base64(*args, **kwargs): # real signature unknown
    """ Base64-code line of data. """
    pass

def b2a_hex(b, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Hexadecimal representation of binary data.
    
      sep
        An optional single character or byte to separate hex bytes.
      bytes_per_sep
        How many bytes between separators.  Positive values count from the
        right, negative values count from the left.
    
    The return value is a bytes object.  This function is also
    available as "hexlify()".
    
    Example:
    >>> binascii.b2a_hex(b'\xb9\x01\xef')
    b'b901ef'
    >>> binascii.hexlify(b'\xb9\x01\xef', ':')
    b'b9:01:ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
    b'b9_01ef'
    """
    pass

def b2a_qp(*args, **kwargs): # real signature unknown
    """
    Encode a string using quoted-printable encoding.
    
    On encoding, when istext is set, newlines are not encoded, and white
    space at end of lines is.  When istext is not set, \r and \n (CR/LF)
    are both encoded.  When quotetabs is set, space and tabs are encoded.
    """
    pass

def b2a_uu(*args, **kwargs): # real signature unknown
    """ Uuencode line of data. """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """ Compute CRC-32 incrementally. """
    pass

def crc_hqx(*args, **kwargs): # real signature unknown
    """ Compute CRC-CCITT incrementally. """
    pass

def hexlify(data): # known case of binascii.hexlify
    """
    Hexadecimal representation of binary data.
    
      sep
        An optional single character or byte to separate hex bytes.
      bytes_per_sep
        How many bytes between separators.  Positive values count from the
        right, negative values count from the left.
    
    The return value is a bytes object.  This function is also
    available as "b2a_hex()".
    """
    return b""

def unhexlify(hexstr): # known case of binascii.unhexlify
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    """
    return b""

# classes

class Error(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class Incomplete(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fabfa950>'

__spec__ = None # (!) real value is "ModuleSpec(name='binascii', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fabfa950>, origin='/usr/lib/python3.11/lib-dynload/binascii.cpython-311-x86_64-linux-gnu.so')"

