# encoding: utf-8
# module greenlet._greenlet
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/greenlet/_greenlet.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import greenlet as __greenlet


# Variables with simple values

CLOCKS_PER_SEC = 1000000

GREENLET_USE_CONTEXT_VARS = True

GREENLET_USE_GC = True

GREENLET_USE_STANDARD_THREADING = True

GREENLET_USE_TRACING = True

# functions

def enable_optional_cleanup(bool): # real signature unknown; restored from __doc__
    """
    mod_enable_optional_cleanup(bool) -> None
    
    Enable or disable optional cleanup operations.
    See ``get_clocks_used_doing_optional_cleanup()`` for details.
    """
    pass

def getcurrent(): # real signature unknown; restored from __doc__
    """
    getcurrent() -> greenlet
    
    Returns the current greenlet (i.e. the one which called this function).
    """
    return greenlet

def gettrace(): # real signature unknown; restored from __doc__
    """
    gettrace() -> object
    
    Returns the currently set tracing function, or None.
    """
    return object()

def get_clocks_used_doing_optional_cleanup(): # real signature unknown; restored from __doc__
    """
    get_clocks_used_doing_optional_cleanup() -> Integer
    
    Get the number of clock ticks the program has used doing optional greenlet cleanup.
    Beginning in greenlet 2.0, greenlet tries to find and dispose of greenlets
    that leaked after a thread exited. This requires invoking Python's garbage collector,
    which may have a performance cost proportional to the number of live objects.
    This function returns the amount of processor time
    greenlet has used to do this. In programs that run with very large amounts of live
    objects, this metric can be used to decide whether the cost of doing this cleanup
    is worth the memory leak being corrected. If not, you can disable the cleanup
    using ``enable_optional_cleanup(False)``.
    The units are arbitrary and can only be compared to themselves (similarly to ``time.clock()``);
    for example, to see how it scales with your heap. You can attempt to convert them into seconds
    by dividing by the value of CLOCKS_PER_SEC.If cleanup has been disabled, returns None.
    This is an implementation specific, provisional API. It may be changed or removed
    in the future.
    .. versionadded:: 2.0
    """
    return 0

def get_pending_cleanup_count(): # real signature unknown; restored from __doc__
    """
    get_pending_cleanup_count() -> Integer
    
    Get the number of greenlet cleanup operations pending. Testing only.
    """
    return 0

def get_total_main_greenlets(): # real signature unknown; restored from __doc__
    """
    get_total_main_greenlets() -> Integer
    
    Quickly return the number of main greenlets that exist. Testing only.
    """
    return 0

def get_tstate_trash_delete_nesting(): # real signature unknown; restored from __doc__
    """
    get_tstate_trash_delete_nesting() -> Integer
    
    Return the 'trash can' nesting level. Testing only.
    """
    return 0

def settrace(callback): # real signature unknown; restored from __doc__
    """
    settrace(callback) -> object
    
    Sets a new tracing function and returns the previous one.
    """
    return object()

def set_thread_local(key, value): # real signature unknown; restored from __doc__
    """
    set_thread_local(key, value) -> None
    
    Set a value in the current thread-local dictionary. Debugging only.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class greenlet(object):
    """
    greenlet(run=None, parent=None) -> greenlet
    
    Creates a new greenlet object (without running it).
    
     - *run* -- The callable to invoke.
     - *parent* -- The parent greenlet. The default is the current greenlet.
    """
    def getcurrent(self): # real signature unknown; restored from __doc__
        """
        getcurrent() -> greenlet
        
        Returns the current greenlet (i.e. the one which called this function).
        """
        return greenlet

    def gettrace(self): # real signature unknown; restored from __doc__
        """
        gettrace() -> object
        
        Returns the currently set tracing function, or None.
        """
        return object()

    def settrace(self, callback): # real signature unknown; restored from __doc__
        """
        settrace(callback) -> object
        
        Sets a new tracing function and returns the previous one.
        """
        return object()

    def switch(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        switch(*args, **kwargs)
        
        Switch execution to this greenlet.
        
        If this greenlet has never been run, then this greenlet
        will be switched to using the body of ``self.run(*args, **kwargs)``.
        
        If the greenlet is active (has been run, but was switch()'ed
        out before leaving its run function), then this greenlet will
        be resumed and the return value to its switch call will be
        None if no arguments are given, the given argument if one
        argument is given, or the args tuple and keyword args dict if
        multiple arguments are given.
        
        If the greenlet is dead, or is the current greenlet then this
        function will simply return the arguments using the same rules as
        above.
        """
        pass

    def throw(self, *args, **kwargs): # real signature unknown
        """
        Switches execution to this greenlet, but immediately raises the
        given exception in this greenlet.  If no argument is provided, the exception
        defaults to `greenlet.GreenletExit`.  The normal exception
        propagation rules apply, as described for `switch`.  Note that calling this
        method is almost equivalent to the following::
        
            def raiser():
                raise typ, val, tb
            g_raiser = greenlet(raiser, parent=g)
            g_raiser.switch()
        
        except that this trick does not work for the
        `greenlet.GreenletExit` exception, which would not propagate
        from ``g_raiser`` to ``g``.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, run=None, parent=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    dead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gr_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _stack_saved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    error = error
    GreenletExit = None # (!) forward: GreenletExit, real value is "<class 'greenlet.GreenletExit'>"
    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x7ff7b4150c60>, '__repr__': <slot wrapper '__repr__' of 'greenlet.greenlet' objects>, '__init__': <slot wrapper '__init__' of 'greenlet.greenlet' objects>, '__bool__': <slot wrapper '__bool__' of 'greenlet.greenlet' objects>, 'switch': <method 'switch' of 'greenlet.greenlet' objects>, 'throw': <method 'throw' of 'greenlet.greenlet' objects>, '__getstate__': <method '__getstate__' of 'greenlet.greenlet' objects>, '__dict__': <attribute '__dict__' of 'greenlet.greenlet' objects>, 'run': <attribute 'run' of 'greenlet.greenlet' objects>, 'parent': <attribute 'parent' of 'greenlet.greenlet' objects>, 'gr_frame': <attribute 'gr_frame' of 'greenlet.greenlet' objects>, 'gr_context': <attribute 'gr_context' of 'greenlet.greenlet' objects>, 'dead': <attribute 'dead' of 'greenlet.greenlet' objects>, '_stack_saved': <attribute '_stack_saved' of 'greenlet.greenlet' objects>, '__doc__': 'greenlet(run=None, parent=None) -> greenlet\\n\\nCreates a new greenlet object (without running it).\\n\\n - *run* -- The callable to invoke.\\n - *parent* -- The parent greenlet. The default is the current greenlet.', 'getcurrent': <built-in function getcurrent>, 'error': <class 'greenlet.error'>, 'GreenletExit': <class 'greenlet.GreenletExit'>, 'settrace': <built-in function settrace>, 'gettrace': <built-in function gettrace>})"


class GreenletExit(BaseException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class UnswitchableGreenlet(__greenlet.greenlet):
    """ Undocumented internal class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    force_slp_switch_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_switch_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

_C_API = None # (!) real value is '<capsule object "greenlet._C_API" at 0x7ff7b3aaf870>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b3add910>'

__spec__ = None # (!) real value is "ModuleSpec(name='greenlet._greenlet', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b3add910>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/greenlet/_greenlet.cpython-311-x86_64-linux-gnu.so')"

