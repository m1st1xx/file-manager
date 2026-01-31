# encoding: utf-8
# module readline
# from /usr/lib/python3.11/lib-dynload/readline.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
""" Importing this module enables command line editing using GNU readline. """
# no imports

# Variables with simple values

_READLINE_LIBRARY_VERSION = '8.2'

_READLINE_RUNTIME_VERSION = 2050

_READLINE_VERSION = 2050

# functions

def add_history(*args, **kwargs): # real signature unknown
    """ Add an item to the history buffer. """
    pass

def append_history_file(*args, **kwargs): # real signature unknown
    """
    Append the last nelements items of the history list to file.
    
    The default filename is ~/.history.
    """
    pass

def clear_history(*args, **kwargs): # real signature unknown
    """ Clear the current readline history. """
    pass

def get_begidx(*args, **kwargs): # real signature unknown
    """ Get the beginning index of the completion scope. """
    pass

def get_completer(*args, **kwargs): # real signature unknown
    """ Get the current completer function. """
    pass

def get_completer_delims(*args, **kwargs): # real signature unknown
    """ Get the word delimiters for completion. """
    pass

def get_completion_type(*args, **kwargs): # real signature unknown
    """ Get the type of completion being attempted. """
    pass

def get_current_history_length(*args, **kwargs): # real signature unknown
    """ Return the current (not the maximum) length of history. """
    pass

def get_endidx(*args, **kwargs): # real signature unknown
    """ Get the ending index of the completion scope. """
    pass

def get_history_item(*args, **kwargs): # real signature unknown
    """ Return the current contents of history item at one-based index. """
    pass

def get_history_length(*args, **kwargs): # real signature unknown
    """ Return the maximum number of lines that will be written to the history file. """
    pass

def get_line_buffer(*args, **kwargs): # real signature unknown
    """ Return the current contents of the line buffer. """
    pass

def insert_text(*args, **kwargs): # real signature unknown
    """ Insert text into the line buffer at the cursor position. """
    pass

def parse_and_bind(*args, **kwargs): # real signature unknown
    """ Execute the init line provided in the string argument. """
    pass

def read_history_file(*args, **kwargs): # real signature unknown
    """
    Load a readline history file.
    
    The default filename is ~/.history.
    """
    pass

def read_init_file(*args, **kwargs): # real signature unknown
    """
    Execute a readline initialization file.
    
    The default filename is the last filename used.
    """
    pass

def redisplay(*args, **kwargs): # real signature unknown
    """ Change what's displayed on the screen to reflect contents of the line buffer. """
    pass

def remove_history_item(*args, **kwargs): # real signature unknown
    """ Remove history item given by its zero-based position. """
    pass

def replace_history_item(*args, **kwargs): # real signature unknown
    """
    Replaces history item given by its position with contents of line.
    
    pos is zero-based.
    """
    pass

def set_auto_history(*args, **kwargs): # real signature unknown
    """ Enables or disables automatic history. """
    pass

def set_completer(*args, **kwargs): # real signature unknown
    """
    Set or remove the completer function.
    
    The function is called as function(text, state),
    for state in 0, 1, 2, ..., until it returns a non-string.
    It should return the next possible completion starting with 'text'.
    """
    pass

def set_completer_delims(*args, **kwargs): # real signature unknown
    """ Set the word delimiters for completion. """
    pass

def set_completion_display_matches_hook(*args, **kwargs): # real signature unknown
    """
    Set or remove the completion display function.
    
    The function is called as
      function(substitution, [matches], longest_match_length)
    once each time matches need to be displayed.
    """
    pass

def set_history_length(*args, **kwargs): # real signature unknown
    """
    Set the maximal number of lines which will be written to the history file.
    
    A negative length is used to inhibit history truncation.
    """
    pass

def set_pre_input_hook(*args, **kwargs): # real signature unknown
    """
    Set or remove the function invoked by the rl_pre_input_hook callback.
    
    The function is called with no arguments after the first prompt
    has been printed and just before readline starts reading input
    characters.
    """
    pass

def set_startup_hook(*args, **kwargs): # real signature unknown
    """
    Set or remove the function invoked by the rl_startup_hook callback.
    
    The function is called with no arguments just
    before readline prints the first prompt.
    """
    pass

def write_history_file(*args, **kwargs): # real signature unknown
    """
    Save a readline history file.
    
    The default filename is ~/.history.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab88d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='readline', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab88d0>, origin='/usr/lib/python3.11/lib-dynload/readline.cpython-311-x86_64-linux-gnu.so')"

