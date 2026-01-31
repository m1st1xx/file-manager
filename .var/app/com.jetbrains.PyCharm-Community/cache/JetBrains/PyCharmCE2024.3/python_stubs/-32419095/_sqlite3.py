# encoding: utf-8
# module _sqlite3
# from /usr/lib/python3.11/lib-dynload/_sqlite3.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import sqlite3 as __sqlite3


# Variables with simple values

PARSE_COLNAMES = 2
PARSE_DECLTYPES = 1

SQLITE_ABORT = 4

SQLITE_ABORT_ROLLBACK = 516

SQLITE_ALTER_TABLE = 26

SQLITE_ANALYZE = 28
SQLITE_ATTACH = 24
SQLITE_AUTH = 23

SQLITE_AUTH_USER = 279

SQLITE_BUSY = 5

SQLITE_BUSY_RECOVERY = 261
SQLITE_BUSY_SNAPSHOT = 517
SQLITE_BUSY_TIMEOUT = 773

SQLITE_CANTOPEN = 14

SQLITE_CANTOPEN_CONVPATH = 1038
SQLITE_CANTOPEN_DIRTYWAL = 1294
SQLITE_CANTOPEN_FULLPATH = 782
SQLITE_CANTOPEN_ISDIR = 526
SQLITE_CANTOPEN_NOTEMPDIR = 270
SQLITE_CANTOPEN_SYMLINK = 1550

SQLITE_CONSTRAINT = 19

SQLITE_CONSTRAINT_CHECK = 275
SQLITE_CONSTRAINT_COMMITHOOK = 531
SQLITE_CONSTRAINT_FOREIGNKEY = 787
SQLITE_CONSTRAINT_FUNCTION = 1043
SQLITE_CONSTRAINT_NOTNULL = 1299
SQLITE_CONSTRAINT_PINNED = 2835
SQLITE_CONSTRAINT_PRIMARYKEY = 1555
SQLITE_CONSTRAINT_ROWID = 2579
SQLITE_CONSTRAINT_TRIGGER = 1811
SQLITE_CONSTRAINT_UNIQUE = 2067
SQLITE_CONSTRAINT_VTAB = 2323

SQLITE_CORRUPT = 11

SQLITE_CORRUPT_INDEX = 779
SQLITE_CORRUPT_SEQUENCE = 523
SQLITE_CORRUPT_VTAB = 267

SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2

SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6

SQLITE_CREATE_TRIGGER = 7
SQLITE_CREATE_VIEW = 8
SQLITE_CREATE_VTABLE = 29

SQLITE_DELETE = 9
SQLITE_DENY = 1
SQLITE_DETACH = 25
SQLITE_DONE = 101

SQLITE_DROP_INDEX = 10
SQLITE_DROP_TABLE = 11

SQLITE_DROP_TEMP_INDEX = 12
SQLITE_DROP_TEMP_TABLE = 13
SQLITE_DROP_TEMP_TRIGGER = 14
SQLITE_DROP_TEMP_VIEW = 15

SQLITE_DROP_TRIGGER = 16
SQLITE_DROP_VIEW = 17
SQLITE_DROP_VTABLE = 30

SQLITE_EMPTY = 16
SQLITE_ERROR = 1

SQLITE_ERROR_MISSING_COLLSEQ = 257

SQLITE_ERROR_RETRY = 513
SQLITE_ERROR_SNAPSHOT = 769

SQLITE_FORMAT = 24
SQLITE_FULL = 13
SQLITE_FUNCTION = 31
SQLITE_IGNORE = 2
SQLITE_INSERT = 18
SQLITE_INTERNAL = 2
SQLITE_INTERRUPT = 9
SQLITE_IOERR = 10

SQLITE_IOERR_ACCESS = 3338
SQLITE_IOERR_AUTH = 7178

SQLITE_IOERR_BEGIN_ATOMIC = 7434

SQLITE_IOERR_BLOCKED = 2826
SQLITE_IOERR_CHECKRESERVEDLOCK = 3594
SQLITE_IOERR_CLOSE = 4106

SQLITE_IOERR_COMMIT_ATOMIC = 7690

SQLITE_IOERR_CONVPATH = 6666
SQLITE_IOERR_CORRUPTFS = 8458
SQLITE_IOERR_DATA = 8202
SQLITE_IOERR_DELETE = 2570

SQLITE_IOERR_DELETE_NOENT = 5898

SQLITE_IOERR_DIR_CLOSE = 4362
SQLITE_IOERR_DIR_FSYNC = 1290

SQLITE_IOERR_FSTAT = 1802
SQLITE_IOERR_FSYNC = 1034
SQLITE_IOERR_GETTEMPPATH = 6410
SQLITE_IOERR_LOCK = 3850
SQLITE_IOERR_MMAP = 6154
SQLITE_IOERR_NOMEM = 3082
SQLITE_IOERR_RDLOCK = 2314
SQLITE_IOERR_READ = 266

SQLITE_IOERR_ROLLBACK_ATOMIC = 7946

SQLITE_IOERR_SEEK = 5642
SQLITE_IOERR_SHMLOCK = 5130
SQLITE_IOERR_SHMMAP = 5386
SQLITE_IOERR_SHMOPEN = 4618
SQLITE_IOERR_SHMSIZE = 4874

SQLITE_IOERR_SHORT_READ = 522

SQLITE_IOERR_TRUNCATE = 1546
SQLITE_IOERR_UNLOCK = 2058
SQLITE_IOERR_VNODE = 6922
SQLITE_IOERR_WRITE = 778

SQLITE_LIMIT_ATTACHED = 7
SQLITE_LIMIT_COLUMN = 2

SQLITE_LIMIT_COMPOUND_SELECT = 4

SQLITE_LIMIT_EXPR_DEPTH = 3

SQLITE_LIMIT_FUNCTION_ARG = 6

SQLITE_LIMIT_LENGTH = 0

SQLITE_LIMIT_LIKE_PATTERN_LENGTH = 8

SQLITE_LIMIT_SQL_LENGTH = 1

SQLITE_LIMIT_TRIGGER_DEPTH = 10

SQLITE_LIMIT_VARIABLE_NUMBER = 9

SQLITE_LIMIT_VDBE_OP = 5

SQLITE_LIMIT_WORKER_THREADS = 11

SQLITE_LOCKED = 6

SQLITE_LOCKED_SHAREDCACHE = 262
SQLITE_LOCKED_VTAB = 518

SQLITE_MISMATCH = 20
SQLITE_MISUSE = 21
SQLITE_NOLFS = 22
SQLITE_NOMEM = 7
SQLITE_NOTADB = 26
SQLITE_NOTFOUND = 12
SQLITE_NOTICE = 27

SQLITE_NOTICE_RECOVER_ROLLBACK = 539
SQLITE_NOTICE_RECOVER_WAL = 283

SQLITE_OK = 0

SQLITE_OK_LOAD_PERMANENTLY = 256

SQLITE_OK_SYMLINK = 512

SQLITE_PERM = 3
SQLITE_PRAGMA = 19
SQLITE_PROTOCOL = 15
SQLITE_RANGE = 25
SQLITE_READ = 20
SQLITE_READONLY = 8

SQLITE_READONLY_CANTINIT = 1288
SQLITE_READONLY_CANTLOCK = 520
SQLITE_READONLY_DBMOVED = 1032
SQLITE_READONLY_DIRECTORY = 1544
SQLITE_READONLY_RECOVERY = 264
SQLITE_READONLY_ROLLBACK = 776

SQLITE_RECURSIVE = 33
SQLITE_REINDEX = 27
SQLITE_ROW = 100
SQLITE_SAVEPOINT = 32
SQLITE_SCHEMA = 17
SQLITE_SELECT = 21
SQLITE_TOOBIG = 18
SQLITE_TRANSACTION = 22
SQLITE_UPDATE = 23

sqlite_version = '3.42.0'

SQLITE_WARNING = 28

SQLITE_WARNING_AUTOINDEX = 284

threadsafety = 3

version = '2.6.0'

# functions

def adapt(*args, **kwargs): # real signature unknown
    """ Adapt given object to given protocol. """
    pass

def complete_statement(*args, **kwargs): # real signature unknown
    """ Checks if a string contains a complete SQL statement. """
    pass

def connect(*args, **kwargs): # real signature unknown
    """
    Opens a connection to the SQLite database file database.
    
    You can use ":memory:" to open a database connection to a database that resides
    in RAM instead of on disk.
    """
    pass

def enable_callback_tracebacks(*args, **kwargs): # real signature unknown
    """ Enable or disable callback functions throwing errors to stderr. """
    pass

def enable_shared_cache(*args, **kwargs): # real signature unknown
    """
    Enable or disable shared cache mode for the calling thread.
    
    This method is deprecated and will be removed in Python 3.12.
    Shared cache is strongly discouraged by the SQLite 3 documentation.
    If shared cache must be used, open the database in URI mode using
    the cache=shared query parameter.
    """
    pass

def register_adapter(*args, **kwargs): # real signature unknown
    """ Register a function to adapt Python objects to SQLite values. """
    pass

def register_converter(*args, **kwargs): # real signature unknown
    """ Register a function to convert SQLite values to Python objects. """
    pass

# classes

class Blob(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        """ Close the blob. """
        pass

    def read(self): # real signature unknown; restored from __doc__
        """
        Read data at the current offset position.
        
          length
            Read length in bytes.
        
        If the end of the blob is reached, the data up to end of file will be returned.
        When length is not specified, or is negative, Blob.read() will read until the
        end of the blob.
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Set the current access position to offset.
        
        The origin argument defaults to os.SEEK_SET (absolute blob positioning).
        Other values for origin are os.SEEK_CUR (seek relative to the current position)
        and os.SEEK_END (seek relative to the blob's end).
        """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """ Return the current access position for the blob. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write data at the current offset.
        
        This function cannot change the blob length.  Writing beyond the end of the
        blob will result in an exception being raised.
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Blob context manager enter. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Blob context manager exit. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class Connection(object):
    """ SQLite database connection object. """
    def backup(self, *args, **kwargs): # real signature unknown
        """ Makes a backup of the database. """
        pass

    def blobopen(self, *args, **kwargs): # real signature unknown
        """
        Open and return a BLOB object.
        
          table
            Table name.
          column
            Column name.
          row
            Row index.
          readonly
            Open the BLOB without write permissions.
          name
            Database name.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the database connection.
        
        Any pending transaction is not committed implicitly.
        """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """
        Commit any pending transaction to the database.
        
        If there is no open transaction, this method is a no-op.
        """
        pass

    def create_aggregate(self, *args, **kwargs): # real signature unknown
        """ Creates a new aggregate. """
        pass

    def create_collation(self, *args, **kwargs): # real signature unknown
        """ Creates a collation function. """
        pass

    def create_function(self, *args, **kwargs): # real signature unknown
        """ Creates a new function. """
        pass

    def create_window_function(self, *args, **kwargs): # real signature unknown
        """
        Creates or redefines an aggregate window function. Non-standard.
        
          name
            The name of the SQL aggregate window function to be created or
            redefined.
          num_params
            The number of arguments the step and inverse methods takes.
          aggregate_class
            A class with step(), finalize(), value(), and inverse() methods.
            Set to None to clear the window function.
        """
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        """ Return a cursor for the connection. """
        pass

    def deserialize(self, *args, **kwargs): # real signature unknown
        """
        Load a serialized database.
        
          data
            The serialized database content.
          name
            Which database to reopen with the deserialization.
        
        The deserialize interface causes the database connection to disconnect from the
        target database, and then reopen it as an in-memory database based on the given
        serialized data.
        
        The deserialize interface will fail with SQLITE_BUSY if the database is
        currently in a read transaction or is involved in a backup operation.
        """
        pass

    def enable_load_extension(self, *args, **kwargs): # real signature unknown
        """ Enable dynamic loading of SQLite extension modules. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes an SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes an SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes multiple SQL statements at once. """
        pass

    def getlimit(self, *args, **kwargs): # real signature unknown
        """
        Get connection run-time limits.
        
          category
            The limit category to be queried.
        """
        pass

    def interrupt(self, *args, **kwargs): # real signature unknown
        """ Abort any pending database operation. """
        pass

    def iterdump(self, *args, **kwargs): # real signature unknown
        """ Returns iterator to the dump of the database in an SQL text format. """
        pass

    def load_extension(self, *args, **kwargs): # real signature unknown
        """ Load SQLite extension module. """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """
        Roll back to the start of any pending transaction.
        
        If there is no open transaction, this method is a no-op.
        """
        pass

    def serialize(self, *args, **kwargs): # real signature unknown
        """
        Serialize a database into a byte string.
        
          name
            Which database to serialize.
        
        For an ordinary on-disk database file, the serialization is just a copy of the
        disk file. For an in-memory database or a "temp" database, the serialization is
        the same sequence of bytes which would be written to disk if that database
        were backed up to disk.
        """
        pass

    def setlimit(self, *args, **kwargs): # real signature unknown
        """
        Set connection run-time limits.
        
          category
            The limit category to be set.
          limit
            The new limit. If the new limit is a negative number, the limit is
            unchanged.
        
        Attempts to increase a limit above its hard upper bound are silently truncated
        to the hard upper bound. Regardless of whether or not the limit was changed,
        the prior value of the limit is returned.
        """
        pass

    def set_authorizer(self, *args, **kwargs): # real signature unknown
        """ Sets authorizer callback. """
        pass

    def set_progress_handler(self, *args, **kwargs): # real signature unknown
        """ Sets progress handler callback. """
        pass

    def set_trace_callback(self, *args, **kwargs): # real signature unknown
        """ Sets a trace callback called for each SQL statement (passed as unicode). """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        Called when the connection is used as a context manager.
        
        Returns itself as a convenience to the caller.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        Called when the connection is used as a context manager.
        
        If there was any exception, a rollback takes place; otherwise we commit.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    DatabaseError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IntegrityError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InterfaceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NotSupportedError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OperationalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProgrammingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Cursor(object):
    """ SQLite database cursor class. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the cursor. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes an SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes an SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes multiple SQL statements at once. """
        pass

    def fetchall(self, *args, **kwargs): # real signature unknown
        """ Fetches all rows from the resultset. """
        pass

    def fetchmany(self, *args, **kwargs): # real signature unknown
        """
        Fetches several rows from the resultset.
        
          size
            The default value is set by the Cursor.arraysize attribute.
        """
        pass

    def fetchone(self, *args, **kwargs): # real signature unknown
        """ Fetches one row from the resultset. """
        pass

    def setinputsizes(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in sqlite3. """
        pass

    def setoutputsize(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in sqlite3. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lastrowid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class DatabaseError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class IntegrityError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class PrepareProtocol(object):
    """ PEP 246 style object adaption protocol type. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ProgrammingError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Row(object):
    # no doc
    def keys(self, *args, **kwargs): # real signature unknown
        """ Returns the keys of the row. """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass


class Warning(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

adapters = {
    (
        None, # (!) real value is "<class 'datetime.date'>"
        PrepareProtocol,
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_date at 0x7f25fa7b96c0>'
    ,
    (
        None, # (!) real value is "<class 'datetime.datetime'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_datetime at 0x7f25fa7b9940>'
    ,
}

converters = {
    'DATE': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_date at 0x7f25fa7b9800>'
    'TIMESTAMP': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_timestamp at 0x7f25fa7b98a0>'
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab8890>'

__spec__ = None # (!) real value is "ModuleSpec(name='_sqlite3', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faab8890>, origin='/usr/lib/python3.11/lib-dynload/_sqlite3.cpython-311-x86_64-linux-gnu.so')"

