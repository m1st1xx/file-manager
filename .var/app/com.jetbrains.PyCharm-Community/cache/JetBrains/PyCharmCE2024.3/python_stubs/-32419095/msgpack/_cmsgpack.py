# encoding: utf-8
# module msgpack._cmsgpack
# from /app/lib/python3.11/site-packages/msgpack/_cmsgpack.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # /usr/lib/python3.11/datetime.py
import msgpack.exceptions as __msgpack_exceptions


# functions

def default_read_extended_type(typecode, data): # real signature unknown; restored from __doc__
    """ default_read_extended_type(typecode, data) """
    pass

def unpackb(packed, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unpackb(packed, *, object_hook=None, list_hook=None, bool use_list=True, bool raw=False, int timestamp=0, bool strict_map_key=True, unicode_errors=None, object_pairs_hook=None, ext_hook=ExtType, Py_ssize_t max_str_len=-1, Py_ssize_t max_bin_len=-1, Py_ssize_t max_array_len=-1, Py_ssize_t max_map_len=-1, Py_ssize_t max_ext_len=-1)
    
        Unpack packed_bytes to object. Returns an unpacked object.
    
        Raises ``ExtraData`` when *packed* contains extra bytes.
        Raises ``ValueError`` when *packed* is incomplete.
        Raises ``FormatError`` when *packed* is not valid msgpack.
        Raises ``StackError`` when *packed* contains too nested.
        Other exceptions can be raised during unpacking.
    
        See :class:`Unpacker` for options.
    
        *max_xxx_len* options are configured automatically from ``len(packed)``.
    """
    pass

# classes

class BufferFull(__msgpack_exceptions.UnpackException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ExtraData(ValueError):
    """
    ExtraData is raised when there is trailing data.
    
        This exception is raised while only one-shot (not streaming)
        unpack.
    """
    def __init__(self, unpacked, extra): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class FormatError(ValueError, __msgpack_exceptions.UnpackException):
    """ Invalid msgpack format """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class OutOfData(__msgpack_exceptions.UnpackException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Packer(object):
    """
    Packer(default=None, *, bool use_single_float=False, bool autoreset=True, bool use_bin_type=True, bool strict_types=False, bool datetime=False, unicode_errors=None)
    
        MessagePack Packer
    
        Usage::
    
            packer = Packer()
            astream.write(packer.pack(a))
            astream.write(packer.pack(b))
    
        Packer's constructor has some keyword arguments:
    
        :param callable default:
            Convert user type to builtin type that Packer supports.
            See also simplejson's document.
    
        :param bool use_single_float:
            Use single precision float type for float. (default: False)
    
        :param bool autoreset:
            Reset buffer after each pack and return its content as `bytes`. (default: True).
            If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.
    
        :param bool use_bin_type:
            Use bin type introduced in msgpack spec 2.0 for bytes.
            It also enables str8 type for unicode. (default: True)
    
        :param bool strict_types:
            If set to true, types will be checked to be exact. Derived classes
            from serializeable types will not be serialized and will be
            treated as unsupported type and forwarded to default.
            Additionally tuples will not be serialized as lists.
            This is useful when trying to implement accurate serialization
            for python types.
    
        :param bool datetime:
            If set to true, datetime with tzinfo is packed into Timestamp type.
            Note that the tzinfo is stripped in the timestamp.
            You can get UTC datetime with `timestamp=3` option of the Unpacker.
            (Python 2 is not supported).
    
        :param str unicode_errors:
            The error handler for encoding unicode. (default: 'strict')
            DO NOT USE THIS!!  This option is kept for very specific usage.
    """
    def bytes(self): # real signature unknown; restored from __doc__
        """
        Packer.bytes(self)
        Return internal buffer contents as bytes object
        """
        pass

    def getbuffer(self): # real signature unknown; restored from __doc__
        """
        Packer.getbuffer(self)
        Return view of internal buffer.
        """
        pass

    def pack(self, obj): # real signature unknown; restored from __doc__
        """ Packer.pack(self, obj) """
        pass

    def pack_array_header(self, long_long_size): # real signature unknown; restored from __doc__
        """ Packer.pack_array_header(self, long long size) """
        pass

    def pack_ext_type(self, typecode, data): # real signature unknown; restored from __doc__
        """ Packer.pack_ext_type(self, typecode, data) """
        pass

    def pack_map_header(self, long_long_size): # real signature unknown; restored from __doc__
        """ Packer.pack_map_header(self, long long size) """
        pass

    def pack_map_pairs(self, pairs): # real signature unknown; restored from __doc__
        """
        Packer.pack_map_pairs(self, pairs)
        
                Pack *pairs* as msgpack map type.
        
                *pairs* should be a sequence of pairs.
                (`len(pairs)` and `for k, v in pairs:` should be supported.)
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        Packer.reset(self)
        Reset internal buffer.
        
                This method is useful only when autoreset=False.
        """
        pass

    def __init__(self, default=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Packer.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Packer.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faac02a0>'


class StackError(ValueError, __msgpack_exceptions.UnpackException):
    """ Too nested """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class Unpacker(object):
    """
    Unpacker(file_like=None, Py_ssize_t read_size=0, *, bool use_list=True, bool raw=False, int timestamp=0, bool strict_map_key=True, object_hook=None, object_pairs_hook=None, list_hook=None, unicode_errors=None, Py_ssize_t max_buffer_size=104857600, ext_hook=ExtType, Py_ssize_t max_str_len=-1, Py_ssize_t max_bin_len=-1, Py_ssize_t max_array_len=-1, Py_ssize_t max_map_len=-1, Py_ssize_t max_ext_len=-1)
    Streaming unpacker.
    
        Arguments:
    
        :param file_like:
            File-like object having `.read(n)` method.
            If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.
    
        :param int read_size:
            Used as `file_like.read(read_size)`. (default: `min(16*1024, max_buffer_size)`)
    
        :param bool use_list:
            If true, unpack msgpack array to Python list.
            Otherwise, unpack to Python tuple. (default: True)
    
        :param bool raw:
            If true, unpack msgpack raw to Python bytes.
            Otherwise, unpack to Python str by decoding with UTF-8 encoding (default).
    
        :param int timestamp:
            Control how timestamp type is unpacked:
    
                0 - Timestamp
                1 - float  (Seconds from the EPOCH)
                2 - int  (Nanoseconds from the EPOCH)
                3 - datetime.datetime  (UTC).  Python 2 is not supported.
    
        :param bool strict_map_key:
            If true (default), only str or bytes are accepted for map (dict) keys.
    
        :param callable object_hook:
            When specified, it should be callable.
            Unpacker calls it with a dict argument after unpacking msgpack map.
            (See also simplejson)
    
        :param callable object_pairs_hook:
            When specified, it should be callable.
            Unpacker calls it with a list of key-value pairs after unpacking msgpack map.
            (See also simplejson)
    
        :param str unicode_errors:
            The error handler for decoding unicode. (default: 'strict')
            This option should be used only when you have msgpack data which
            contains invalid UTF-8 string.
    
        :param int max_buffer_size:
            Limits size of data waiting unpacked.  0 means 2**32-1.
            The default value is 100*1024*1024 (100MiB).
            Raises `BufferFull` exception when it is insufficient.
            You should set this parameter when unpacking data from untrusted source.
    
        :param int max_str_len:
            Deprecated, use *max_buffer_size* instead.
            Limits max length of str. (default: max_buffer_size)
    
        :param int max_bin_len:
            Deprecated, use *max_buffer_size* instead.
            Limits max length of bin. (default: max_buffer_size)
    
        :param int max_array_len:
            Limits max length of array.
            (default: max_buffer_size)
    
        :param int max_map_len:
            Limits max length of map.
            (default: max_buffer_size//2)
    
        :param int max_ext_len:
            Deprecated, use *max_buffer_size* instead.
            Limits max size of ext type.  (default: max_buffer_size)
    
        Example of streaming deserialize from file-like object::
    
            unpacker = Unpacker(file_like)
            for o in unpacker:
                process(o)
    
        Example of streaming deserialize from socket::
    
            unpacker = Unpacker()
            while True:
                buf = sock.recv(1024**2)
                if not buf:
                    break
                unpacker.feed(buf)
                for o in unpacker:
                    process(o)
    
        Raises ``ExtraData`` when *packed* contains extra bytes.
        Raises ``OutOfData`` when *packed* is incomplete.
        Raises ``FormatError`` when *packed* is not valid msgpack.
        Raises ``StackError`` when *packed* contains too nested.
        Other exceptions can be raised during unpacking.
    """
    def feed(self, next_bytes): # real signature unknown; restored from __doc__
        """
        Unpacker.feed(self, next_bytes)
        Append `next_bytes` to internal buffer.
        """
        pass

    def read_array_header(self): # real signature unknown; restored from __doc__
        """
        Unpacker.read_array_header(self)
        assuming the next object is an array, return its size n, such that
                the next n unpack() calls will iterate over its contents.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def read_bytes(self, Py_ssize_t_nbytes): # real signature unknown; restored from __doc__
        """
        Unpacker.read_bytes(self, Py_ssize_t nbytes)
        Read a specified number of raw bytes from the stream
        """
        pass

    def read_map_header(self): # real signature unknown; restored from __doc__
        """
        Unpacker.read_map_header(self)
        assuming the next object is a map, return its size n, such that the
                next n * 2 unpack() calls will iterate over its key-value pairs.
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def skip(self): # real signature unknown; restored from __doc__
        """
        Unpacker.skip(self)
        Read and ignore one object, returning None
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """
        Unpacker.tell(self)
        Returns the current position of the Unpacker in bytes, i.e., the
                number of bytes that were read from the input, also the starting
                position of the next object.
        """
        pass

    def unpack(self): # real signature unknown; restored from __doc__
        """
        Unpacker.unpack(self)
        Unpack one object
        
                Raises `OutOfData` when there are no more bytes to unpack.
        """
        pass

    def __init__(self, file_like=None, Py_ssize_t_read_size=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Unpacker.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Unpacker.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faac0150>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab9a50>'

__spec__ = None # (!) real value is "ModuleSpec(name='msgpack._cmsgpack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab9a50>, origin='/app/lib/python3.11/site-packages/msgpack/_cmsgpack.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

