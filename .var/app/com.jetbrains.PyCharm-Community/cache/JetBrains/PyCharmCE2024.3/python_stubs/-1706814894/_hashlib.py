# encoding: utf-8
# module _hashlib
# from /usr/lib/python3.11/lib-dynload/_hashlib.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
""" OpenSSL interface for hashlib module """
# no imports

# functions

def compare_digest(*args, **kwargs): # real signature unknown
    """
    Return 'a == b'.
    
    This function uses an approach designed to prevent
    timing analysis, making it appropriate for cryptography.
    
    a and b must both be of the same type: either str (ASCII only),
    or any bytes-like object.
    
    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b--but not their values.
    """
    pass

def get_fips_mode(*args, **kwargs): # real signature unknown
    """
    Determine the OpenSSL FIPS mode of operation.
    
    For OpenSSL 3.0.0 and newer it returns the state of the default provider
    in the default OSSL context. It's not quite the same as FIPS_mode() but good
    enough for unittests.
    
    Effectively any non-zero return value indicates FIPS mode;
    values other than 1 may have additional significance.
    """
    pass

def hmac_digest(*args, **kwargs): # real signature unknown
    """ Single-shot HMAC. """
    pass

def hmac_new(*args, **kwargs): # real signature unknown
    """ Return a new hmac object. """
    pass

def new(*args, **kwargs): # real signature unknown
    """
    Return a new hash object using the named algorithm.
    
    An optional string argument may be provided and will be
    automatically hashed.
    
    The MD5 and SHA1 algorithms are always supported.
    """
    pass

def openssl_md5(*args, **kwargs): # real signature unknown
    """ Returns a md5 hash object; optionally initialized with a string """
    pass

def openssl_sha1(*args, **kwargs): # real signature unknown
    """ Returns a sha1 hash object; optionally initialized with a string """
    pass

def openssl_sha224(*args, **kwargs): # real signature unknown
    """ Returns a sha224 hash object; optionally initialized with a string """
    pass

def openssl_sha256(*args, **kwargs): # real signature unknown
    """ Returns a sha256 hash object; optionally initialized with a string """
    pass

def openssl_sha384(*args, **kwargs): # real signature unknown
    """ Returns a sha384 hash object; optionally initialized with a string """
    pass

def openssl_sha3_224(*args, **kwargs): # real signature unknown
    """ Returns a sha3-224 hash object; optionally initialized with a string """
    pass

def openssl_sha3_256(*args, **kwargs): # real signature unknown
    """ Returns a sha3-256 hash object; optionally initialized with a string """
    pass

def openssl_sha3_384(*args, **kwargs): # real signature unknown
    """ Returns a sha3-384 hash object; optionally initialized with a string """
    pass

def openssl_sha3_512(*args, **kwargs): # real signature unknown
    """ Returns a sha3-512 hash object; optionally initialized with a string """
    pass

def openssl_sha512(*args, **kwargs): # real signature unknown
    """ Returns a sha512 hash object; optionally initialized with a string """
    pass

def openssl_shake_128(*args, **kwargs): # real signature unknown
    """ Returns a shake-128 variable hash object; optionally initialized with a string """
    pass

def openssl_shake_256(*args, **kwargs): # real signature unknown
    """ Returns a shake-256 variable hash object; optionally initialized with a string """
    pass

def pbkdf2_hmac(*args, **kwargs): # real signature unknown
    """ Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function. """
    pass

def scrypt(*args, **kwargs): # real signature unknown
    """ scrypt password-based key derivation function. """
    pass

# classes

class HASH(object):
    """
    A hash is an object used to calculate a checksum of a string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided string. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HASHXOF(HASH):
    """
    A hash is an object used to calculate a checksum of a string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest(length) -- return the current digest value
    hexdigest(length) -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HMAC(object):
    """
    The object used to calculate HMAC of a message.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the name, including the hash algorithm used by this object
    digest_size -- number of bytes in digest() output
    """
    def copy(self, clone): # real signature unknown; restored from __doc__
        """ Return a copy ("clone") of the HMAC object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest of the bytes passed to the update() method so far. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """
        Return hexadecimal digest of the bytes passed to the update() method so far.
        
        This may be used to exchange the value safely in email or other non-binary
        environments.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update the HMAC object with msg. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnsupportedDigestmodError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

openssl_md_meth_names = None # (!) real value is "frozenset({'sha3_512', 'sha1', 'blake2s', 'md5-sha1', 'sm3', 'shake_256', 'sha512_224', 'sha3_224', 'sha384', 'sha256', 'ripemd160', 'md5', 'sha3_384', 'sha3_256', 'shake_128', 'blake2b', 'sha512_256', 'sha512', 'sha224'})"

_constructors = None # (!) real value is "mappingproxy({<built-in function openssl_md5>: 'md5', <built-in function openssl_sha1>: 'sha1', <built-in function openssl_sha224>: 'sha224', <built-in function openssl_sha256>: 'sha256', <built-in function openssl_sha384>: 'sha384', <built-in function openssl_sha512>: 'sha512', <built-in function openssl_sha3_224>: 'sha3_224', <built-in function openssl_sha3_256>: 'sha3_256', <built-in function openssl_sha3_384>: 'sha3_384', <built-in function openssl_sha3_512>: 'sha3_512', <built-in function openssl_shake_128>: 'shake_128', <built-in function openssl_shake_256>: 'shake_256'})"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fb2a0a90>'

__spec__ = None # (!) real value is "ModuleSpec(name='_hashlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25fb2a0a90>, origin='/usr/lib/python3.11/lib-dynload/_hashlib.cpython-311-x86_64-linux-gnu.so')"

