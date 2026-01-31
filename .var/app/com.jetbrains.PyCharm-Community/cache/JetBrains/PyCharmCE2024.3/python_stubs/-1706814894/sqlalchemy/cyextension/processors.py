# encoding: utf-8
# module sqlalchemy.cyextension.processors
# from /home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/processors.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # /usr/lib/python3.11/datetime.py
import re as re # /usr/lib/python3.11/re/__init__.py
import datetime as __datetime


# functions

def int_to_boolean(*args, **kwargs): # real signature unknown
    pass

def str_to_date(*args, **kwargs): # real signature unknown
    pass

def str_to_datetime(*args, **kwargs): # real signature unknown
    pass

def str_to_time(*args, **kwargs): # real signature unknown
    pass

def to_float(*args, **kwargs): # real signature unknown
    pass

def to_str(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class date_cls(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromisocalendar(cls, *args, **kwargs): # real signature unknown
        """
        int, int, int -> Construct a date from the ISO year, week number and weekday.
        
        This is the inverse of the date.isocalendar() function
        """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ str -> Construct a date from a string in ISO 8601 format. """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """
        Create a date from a POSIX timestamp.
        
        The timestamp is a number, e.g. created via time.time(), that is interpreted
        as local time.
        """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a named tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.date(9999, 12, 31)
    min = datetime.date(1, 1, 1)
    resolution = datetime.timedelta(days=1)


class datetime_cls(__datetime.date):
    """
    datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    
    The year, month and day arguments are required. tzinfo may be None, or an
    instance of a tzinfo subclass. The remaining arguments may be ints.
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """ tz -> convert to local time in new timezone tz """
        pass

    @classmethod
    def combine(cls, *args, **kwargs): # real signature unknown
        """ date, time -> datetime with same date and time fields """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> datetime from a string in most ISO 8601 formats """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp[, tz] -> tz's local time from POSIX timestamp. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        sep is used to separate the year from the time, and defaults to 'T'.
        The optional argument timespec specifies the number of additional terms
        of the time to include. Valid options are 'auto', 'hours', 'minutes',
        'seconds', 'milliseconds' and 'microseconds'.
        """
        pass

    @classmethod
    def now(cls, *args, **kwargs): # real signature unknown
        """
        Returns new datetime object representing current time local to tz.
        
          tz
            Timezone object.
        
        If no tz is specified, uses local timezone.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return datetime with new specified fields. """
        pass

    @classmethod
    def strptime(cls): # real signature unknown; restored from __doc__
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    @classmethod
    def utcfromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ Construct a naive UTC datetime from a POSIX timestamp. """
        pass

    @classmethod
    def utcnow(cls, *args, **kwargs): # real signature unknown
        """ Return a new datetime representing UTC day and time. """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    min = datetime.datetime(1, 1, 1, 0, 0)
    resolution = datetime.timedelta(microseconds=1)


class DecimalResultProcessor(object):
    # no doc
    def process(self, *args, **kwargs): # real signature unknown
        pass

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


class time_cls(object):
    """
    time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
    
    All arguments are optional. tzinfo may be None, or an instance of
    a tzinfo subclass. The remaining arguments may be ints.
    """
    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> time from a string in ISO 8601 format """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        
        The optional argument timespec specifies the number of additional terms
        of the time to include. Valid options are 'auto', 'hours', 'minutes',
        'seconds', 'milliseconds' and 'microseconds'.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return time with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.time(23, 59, 59, 999999)
    min = datetime.time(0, 0)
    resolution = datetime.timedelta(microseconds=1)


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38fa4d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='sqlalchemy.cyextension.processors', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff7b38fa4d0>, origin='/home/m1st/file-manager/venv/lib/python3.11/site-packages/sqlalchemy/cyextension/processors.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

