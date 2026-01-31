# encoding: utf-8
# module _ast
# from (built-in)
# by generator 1.147
# no doc

# imports
import ast as __ast


# Variables with simple values

PyCF_ALLOW_TOP_LEVEL_AWAIT = 8192

PyCF_ONLY_AST = 1024

PyCF_TYPE_COMMENTS = 4096

# no functions
# classes

class AST(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x5614a8187ab0>, '__getattribute__': <slot wrapper '__getattribute__' of 'ast.AST' objects>, '__setattr__': <slot wrapper '__setattr__' of 'ast.AST' objects>, '__delattr__': <slot wrapper '__delattr__' of 'ast.AST' objects>, '__init__': <slot wrapper '__init__' of 'ast.AST' objects>, '__reduce__': <method '__reduce__' of 'ast.AST' objects>, '__dict__': <attribute '__dict__' of 'ast.AST' objects>, '__doc__': None, '__module__': 'ast', '_fields': (), '__match_args__': (), '_attributes': ()})"
    __match_args__ = ()


class operator(__ast.AST):
    """ operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class Add(__ast.operator):
    """ Add """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class alias(__ast.AST):
    """ alias(identifier name, identifier? asname) """
    def __init__(self, identifier_name, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    asname = None
    end_col_offset = None
    end_lineno = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = (
        'name',
        'asname',
    )
    __match_args__ = (
        'name',
        'asname',
    )


class boolop(__ast.AST):
    """ boolop = And | Or """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class And(__ast.boolop):
    """ And """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class stmt(__ast.AST):
    """
    stmt = FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
         | AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
         | ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list)
         | Return(expr? value)
         | Delete(expr* targets)
         | Assign(expr* targets, expr value, string? type_comment)
         | AugAssign(expr target, operator op, expr value)
         | AnnAssign(expr target, expr annotation, expr? value, int simple)
         | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
         | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
         | While(expr test, stmt* body, stmt* orelse)
         | If(expr test, stmt* body, stmt* orelse)
         | With(withitem* items, stmt* body, string? type_comment)
         | AsyncWith(withitem* items, stmt* body, string? type_comment)
         | Match(expr subject, match_case* cases)
         | Raise(expr? exc, expr? cause)
         | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
         | TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
         | Assert(expr test, expr? msg)
         | Import(alias* names)
         | ImportFrom(identifier? module, alias* names, int? level)
         | Global(identifier* names)
         | Nonlocal(identifier* names)
         | Expr(expr value)
         | Pass
         | Break
         | Continue
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    end_col_offset = None
    end_lineno = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()
    __match_args__ = ()


class AnnAssign(__ast.stmt):
    """ AnnAssign(expr target, expr annotation, expr? value, int simple) """
    def __init__(self, expr_target, expr_annotation, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    value = None
    _fields = (
        'target',
        'annotation',
        'value',
        'simple',
    )
    __match_args__ = (
        'target',
        'annotation',
        'value',
        'simple',
    )


class arg(__ast.AST):
    """ arg(identifier arg, expr? annotation, string? type_comment) """
    def __init__(self, identifier_arg, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    annotation = None
    end_col_offset = None
    end_lineno = None
    type_comment = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = (
        'arg',
        'annotation',
        'type_comment',
    )
    __match_args__ = (
        'arg',
        'annotation',
        'type_comment',
    )


class arguments(__ast.AST):
    """ arguments(arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs, expr* kw_defaults, arg? kwarg, expr* defaults) """
    def __init__(self, arg, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    kwarg = None
    vararg = None
    _attributes = ()
    _fields = (
        'posonlyargs',
        'args',
        'vararg',
        'kwonlyargs',
        'kw_defaults',
        'kwarg',
        'defaults',
    )
    __match_args__ = (
        'posonlyargs',
        'args',
        'vararg',
        'kwonlyargs',
        'kw_defaults',
        'kwarg',
        'defaults',
    )


class Assert(__ast.stmt):
    """ Assert(expr test, expr? msg) """
    def __init__(self, expr_test, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    msg = None
    _fields = (
        'test',
        'msg',
    )
    __match_args__ = (
        'test',
        'msg',
    )


class Assign(__ast.stmt):
    """ Assign(expr* targets, expr value, string? type_comment) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    type_comment = None
    _fields = (
        'targets',
        'value',
        'type_comment',
    )
    __match_args__ = (
        'targets',
        'value',
        'type_comment',
    )


class AsyncFor(__ast.stmt):
    """ AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment) """
    def __init__(self, expr_target, expr_iter, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    type_comment = None
    _fields = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )
    __match_args__ = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )


class AsyncFunctionDef(__ast.stmt):
    """ AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment) """
    def __init__(self, identifier_name, arguments_args, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    returns = None
    type_comment = None
    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )
    __match_args__ = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )


class AsyncWith(__ast.stmt):
    """ AsyncWith(withitem* items, stmt* body, string? type_comment) """
    def __init__(self, withitem, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    type_comment = None
    _fields = (
        'items',
        'body',
        'type_comment',
    )
    __match_args__ = (
        'items',
        'body',
        'type_comment',
    )


class expr(__ast.AST):
    """
    expr = BoolOp(boolop op, expr* values)
         | NamedExpr(expr target, expr value)
         | BinOp(expr left, operator op, expr right)
         | UnaryOp(unaryop op, expr operand)
         | Lambda(arguments args, expr body)
         | IfExp(expr test, expr body, expr orelse)
         | Dict(expr* keys, expr* values)
         | Set(expr* elts)
         | ListComp(expr elt, comprehension* generators)
         | SetComp(expr elt, comprehension* generators)
         | DictComp(expr key, expr value, comprehension* generators)
         | GeneratorExp(expr elt, comprehension* generators)
         | Await(expr value)
         | Yield(expr? value)
         | YieldFrom(expr value)
         | Compare(expr left, cmpop* ops, expr* comparators)
         | Call(expr func, expr* args, keyword* keywords)
         | FormattedValue(expr value, int conversion, expr? format_spec)
         | JoinedStr(expr* values)
         | Constant(constant value, string? kind)
         | Attribute(expr value, identifier attr, expr_context ctx)
         | Subscript(expr value, expr slice, expr_context ctx)
         | Starred(expr value, expr_context ctx)
         | Name(identifier id, expr_context ctx)
         | List(expr* elts, expr_context ctx)
         | Tuple(expr* elts, expr_context ctx)
         | Slice(expr? lower, expr? upper, expr? step)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    end_col_offset = None
    end_lineno = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()
    __match_args__ = ()


class Attribute(__ast.expr):
    """ Attribute(expr value, identifier attr, expr_context ctx) """
    def __init__(self, expr_value, identifier_attr, expr_context_ctx): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
        'attr',
        'ctx',
    )
    __match_args__ = (
        'value',
        'attr',
        'ctx',
    )


class AugAssign(__ast.stmt):
    """ AugAssign(expr target, operator op, expr value) """
    def __init__(self, expr_target, operator_op, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'target',
        'op',
        'value',
    )
    __match_args__ = (
        'target',
        'op',
        'value',
    )


class Await(__ast.expr):
    """ Await(expr value) """
    def __init__(self, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class BinOp(__ast.expr):
    """ BinOp(expr left, operator op, expr right) """
    def __init__(self, expr_left, operator_op, expr_right): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'left',
        'op',
        'right',
    )
    __match_args__ = (
        'left',
        'op',
        'right',
    )


class BitAnd(__ast.operator):
    """ BitAnd """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class BitOr(__ast.operator):
    """ BitOr """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class BitXor(__ast.operator):
    """ BitXor """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class BoolOp(__ast.expr):
    """ BoolOp(boolop op, expr* values) """
    def __init__(self, boolop_op, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'op',
        'values',
    )
    __match_args__ = (
        'op',
        'values',
    )


class Break(__ast.stmt):
    """ Break """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Call(__ast.expr):
    """ Call(expr func, expr* args, keyword* keywords) """
    def __init__(self, expr_func, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'func',
        'args',
        'keywords',
    )
    __match_args__ = (
        'func',
        'args',
        'keywords',
    )


class ClassDef(__ast.stmt):
    """ ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list) """
    def __init__(self, identifier_name, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'name',
        'bases',
        'keywords',
        'body',
        'decorator_list',
    )
    __match_args__ = (
        'name',
        'bases',
        'keywords',
        'body',
        'decorator_list',
    )


class cmpop(__ast.AST):
    """ cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class Compare(__ast.expr):
    """ Compare(expr left, cmpop* ops, expr* comparators) """
    def __init__(self, expr_left, cmpop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'left',
        'ops',
        'comparators',
    )
    __match_args__ = (
        'left',
        'ops',
        'comparators',
    )


class comprehension(__ast.AST):
    """ comprehension(expr target, expr iter, expr* ifs, int is_async) """
    def __init__(self, expr_target, expr_iter, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = (
        'target',
        'iter',
        'ifs',
        'is_async',
    )
    __match_args__ = (
        'target',
        'iter',
        'ifs',
        'is_async',
    )


class Constant(__ast.expr):
    """ Constant(constant value, string? kind) """
    def __init__(self, constant_value, string, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deprecated. Use value instead."""

    s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deprecated. Use value instead."""


    kind = None
    _fields = (
        'value',
        'kind',
    )
    __match_args__ = (
        'value',
        'kind',
    )


class Continue(__ast.stmt):
    """ Continue """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class expr_context(__ast.AST):
    """ expr_context = Load | Store | Del """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class Del(__ast.expr_context):
    """ Del """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Delete(__ast.stmt):
    """ Delete(expr* targets) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'targets',
    )
    __match_args__ = (
        'targets',
    )


class Dict(__ast.expr):
    """ Dict(expr* keys, expr* values) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'keys',
        'values',
    )
    __match_args__ = (
        'keys',
        'values',
    )


class DictComp(__ast.expr):
    """ DictComp(expr key, expr value, comprehension* generators) """
    def __init__(self, expr_key, expr_value, comprehension, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'key',
        'value',
        'generators',
    )
    __match_args__ = (
        'key',
        'value',
        'generators',
    )


class Div(__ast.operator):
    """ Div """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Eq(__ast.cmpop):
    """ Eq """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class excepthandler(__ast.AST):
    """ excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body) """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    end_col_offset = None
    end_lineno = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()
    __match_args__ = ()


class ExceptHandler(__ast.excepthandler):
    """ ExceptHandler(expr? type, identifier? name, stmt* body) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    name = None
    type = None
    _fields = (
        'type',
        'name',
        'body',
    )
    __match_args__ = (
        'type',
        'name',
        'body',
    )


class Expr(__ast.stmt):
    """ Expr(expr value) """
    def __init__(self, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class mod(__ast.AST):
    """
    mod = Module(stmt* body, type_ignore* type_ignores)
        | Interactive(stmt* body)
        | Expression(expr body)
        | FunctionType(expr* argtypes, expr returns)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class Expression(__ast.mod):
    """ Expression(expr body) """
    def __init__(self, expr_body): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'body',
    )
    __match_args__ = (
        'body',
    )


class FloorDiv(__ast.operator):
    """ FloorDiv """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class For(__ast.stmt):
    """ For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment) """
    def __init__(self, expr_target, expr_iter, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    type_comment = None
    _fields = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )
    __match_args__ = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )


class FormattedValue(__ast.expr):
    """ FormattedValue(expr value, int conversion, expr? format_spec) """
    def __init__(self, expr_value, int_conversion, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    format_spec = None
    _fields = (
        'value',
        'conversion',
        'format_spec',
    )
    __match_args__ = (
        'value',
        'conversion',
        'format_spec',
    )


class FunctionDef(__ast.stmt):
    """ FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment) """
    def __init__(self, identifier_name, arguments_args, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    returns = None
    type_comment = None
    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )
    __match_args__ = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )


class FunctionType(__ast.mod):
    """ FunctionType(expr* argtypes, expr returns) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'argtypes',
        'returns',
    )
    __match_args__ = (
        'argtypes',
        'returns',
    )


class GeneratorExp(__ast.expr):
    """ GeneratorExp(expr elt, comprehension* generators) """
    def __init__(self, expr_elt, comprehension, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'elt',
        'generators',
    )
    __match_args__ = (
        'elt',
        'generators',
    )


class Global(__ast.stmt):
    """ Global(identifier* names) """
    def __init__(self, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'names',
    )
    __match_args__ = (
        'names',
    )


class Gt(__ast.cmpop):
    """ Gt """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class GtE(__ast.cmpop):
    """ GtE """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class If(__ast.stmt):
    """ If(expr test, stmt* body, stmt* orelse) """
    def __init__(self, expr_test, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )
    __match_args__ = (
        'test',
        'body',
        'orelse',
    )


class IfExp(__ast.expr):
    """ IfExp(expr test, expr body, expr orelse) """
    def __init__(self, expr_test, expr_body, expr_orelse): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )
    __match_args__ = (
        'test',
        'body',
        'orelse',
    )


class Import(__ast.stmt):
    """ Import(alias* names) """
    def __init__(self, alias, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'names',
    )
    __match_args__ = (
        'names',
    )


class ImportFrom(__ast.stmt):
    """ ImportFrom(identifier? module, alias* names, int? level) """
    def __init__(self, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    level = None
    module = None
    _fields = (
        'module',
        'names',
        'level',
    )
    __match_args__ = (
        'module',
        'names',
        'level',
    )


class In(__ast.cmpop):
    """ In """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Interactive(__ast.mod):
    """ Interactive(stmt* body) """
    def __init__(self, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'body',
    )
    __match_args__ = (
        'body',
    )


class unaryop(__ast.AST):
    """ unaryop = Invert | Not | UAdd | USub """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class Invert(__ast.unaryop):
    """ Invert """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Is(__ast.cmpop):
    """ Is """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class IsNot(__ast.cmpop):
    """ IsNot """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class JoinedStr(__ast.expr):
    """ JoinedStr(expr* values) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'values',
    )
    __match_args__ = (
        'values',
    )


class keyword(__ast.AST):
    """ keyword(identifier? arg, expr value) """
    def __init__(self, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    arg = None
    end_col_offset = None
    end_lineno = None
    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = (
        'arg',
        'value',
    )
    __match_args__ = (
        'arg',
        'value',
    )


class Lambda(__ast.expr):
    """ Lambda(arguments args, expr body) """
    def __init__(self, arguments_args, expr_body): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'args',
        'body',
    )
    __match_args__ = (
        'args',
        'body',
    )


class List(__ast.expr):
    """ List(expr* elts, expr_context ctx) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'elts',
        'ctx',
    )
    __match_args__ = (
        'elts',
        'ctx',
    )


class ListComp(__ast.expr):
    """ ListComp(expr elt, comprehension* generators) """
    def __init__(self, expr_elt, comprehension, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'elt',
        'generators',
    )
    __match_args__ = (
        'elt',
        'generators',
    )


class Load(__ast.expr_context):
    """ Load """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class LShift(__ast.operator):
    """ LShift """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Lt(__ast.cmpop):
    """ Lt """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class LtE(__ast.cmpop):
    """ LtE """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Match(__ast.stmt):
    """ Match(expr subject, match_case* cases) """
    def __init__(self, expr_subject, match_case, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'subject',
        'cases',
    )
    __match_args__ = (
        'subject',
        'cases',
    )


class pattern(__ast.AST):
    """
    pattern = MatchValue(expr value)
            | MatchSingleton(constant value)
            | MatchSequence(pattern* patterns)
            | MatchMapping(expr* keys, pattern* patterns, identifier? rest)
            | MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)
            | MatchStar(identifier? name)
            | MatchAs(pattern? pattern, identifier? name)
            | MatchOr(pattern* patterns)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()
    __match_args__ = ()


class MatchAs(__ast.pattern):
    """ MatchAs(pattern? pattern, identifier? name) """
    def __init__(self, pattern, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    name = None
    pattern = None
    _fields = (
        'pattern',
        'name',
    )
    __match_args__ = (
        'pattern',
        'name',
    )


class MatchClass(__ast.pattern):
    """ MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns) """
    def __init__(self, expr_cls, pattern, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'cls',
        'patterns',
        'kwd_attrs',
        'kwd_patterns',
    )
    __match_args__ = (
        'cls',
        'patterns',
        'kwd_attrs',
        'kwd_patterns',
    )


class MatchMapping(__ast.pattern):
    """ MatchMapping(expr* keys, pattern* patterns, identifier? rest) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    rest = None
    _fields = (
        'keys',
        'patterns',
        'rest',
    )
    __match_args__ = (
        'keys',
        'patterns',
        'rest',
    )


class MatchOr(__ast.pattern):
    """ MatchOr(pattern* patterns) """
    def __init__(self, pattern, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'patterns',
    )
    __match_args__ = (
        'patterns',
    )


class MatchSequence(__ast.pattern):
    """ MatchSequence(pattern* patterns) """
    def __init__(self, pattern, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'patterns',
    )
    __match_args__ = (
        'patterns',
    )


class MatchSingleton(__ast.pattern):
    """ MatchSingleton(constant value) """
    def __init__(self, constant_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class MatchStar(__ast.pattern):
    """ MatchStar(identifier? name) """
    def __init__(self, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    name = None
    _fields = (
        'name',
    )
    __match_args__ = (
        'name',
    )


class MatchValue(__ast.pattern):
    """ MatchValue(expr value) """
    def __init__(self, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class match_case(__ast.AST):
    """ match_case(pattern pattern, expr? guard, stmt* body) """
    def __init__(self, pattern_pattern, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    guard = None
    _attributes = ()
    _fields = (
        'pattern',
        'guard',
        'body',
    )
    __match_args__ = (
        'pattern',
        'guard',
        'body',
    )


class MatMult(__ast.operator):
    """ MatMult """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Mod(__ast.operator):
    """ Mod """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Module(__ast.mod):
    """ Module(stmt* body, type_ignore* type_ignores) """
    def __init__(self, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'body',
        'type_ignores',
    )
    __match_args__ = (
        'body',
        'type_ignores',
    )


class Mult(__ast.operator):
    """ Mult """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Name(__ast.expr):
    """ Name(identifier id, expr_context ctx) """
    def __init__(self, identifier_id, expr_context_ctx): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'id',
        'ctx',
    )
    __match_args__ = (
        'id',
        'ctx',
    )


class NamedExpr(__ast.expr):
    """ NamedExpr(expr target, expr value) """
    def __init__(self, expr_target, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'target',
        'value',
    )
    __match_args__ = (
        'target',
        'value',
    )


class Nonlocal(__ast.stmt):
    """ Nonlocal(identifier* names) """
    def __init__(self, identifier, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'names',
    )
    __match_args__ = (
        'names',
    )


class Not(__ast.unaryop):
    """ Not """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class NotEq(__ast.cmpop):
    """ NotEq """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class NotIn(__ast.cmpop):
    """ NotIn """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Or(__ast.boolop):
    """ Or """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Pass(__ast.stmt):
    """ Pass """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Pow(__ast.operator):
    """ Pow """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Raise(__ast.stmt):
    """ Raise(expr? exc, expr? cause) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    cause = None
    exc = None
    _fields = (
        'exc',
        'cause',
    )
    __match_args__ = (
        'exc',
        'cause',
    )


class Return(__ast.stmt):
    """ Return(expr? value) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    value = None
    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class RShift(__ast.operator):
    """ RShift """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Set(__ast.expr):
    """ Set(expr* elts) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'elts',
    )
    __match_args__ = (
        'elts',
    )


class SetComp(__ast.expr):
    """ SetComp(expr elt, comprehension* generators) """
    def __init__(self, expr_elt, comprehension, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'elt',
        'generators',
    )
    __match_args__ = (
        'elt',
        'generators',
    )


class Slice(__ast.expr):
    """ Slice(expr? lower, expr? upper, expr? step) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    lower = None
    step = None
    upper = None
    _fields = (
        'lower',
        'upper',
        'step',
    )
    __match_args__ = (
        'lower',
        'upper',
        'step',
    )


class Starred(__ast.expr):
    """ Starred(expr value, expr_context ctx) """
    def __init__(self, expr_value, expr_context_ctx): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
        'ctx',
    )
    __match_args__ = (
        'value',
        'ctx',
    )


class Store(__ast.expr_context):
    """ Store """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Sub(__ast.operator):
    """ Sub """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class Subscript(__ast.expr):
    """ Subscript(expr value, expr slice, expr_context ctx) """
    def __init__(self, expr_value, expr_slice, expr_context_ctx): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
        'slice',
        'ctx',
    )
    __match_args__ = (
        'value',
        'slice',
        'ctx',
    )


class Try(__ast.stmt):
    """ Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody) """
    def __init__(self, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'body',
        'handlers',
        'orelse',
        'finalbody',
    )
    __match_args__ = (
        'body',
        'handlers',
        'orelse',
        'finalbody',
    )


class TryStar(__ast.stmt):
    """ TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody) """
    def __init__(self, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'body',
        'handlers',
        'orelse',
        'finalbody',
    )
    __match_args__ = (
        'body',
        'handlers',
        'orelse',
        'finalbody',
    )


class Tuple(__ast.expr):
    """ Tuple(expr* elts, expr_context ctx) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    dims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deprecated. Use elts instead."""


    _fields = (
        'elts',
        'ctx',
    )
    __match_args__ = (
        'elts',
        'ctx',
    )


class type_ignore(__ast.AST):
    """ type_ignore = TypeIgnore(int lineno, string tag) """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _attributes = ()
    _fields = ()
    __match_args__ = ()


class TypeIgnore(__ast.type_ignore):
    """ TypeIgnore(int lineno, string tag) """
    def __init__(self, int_lineno, string_tag): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'lineno',
        'tag',
    )
    __match_args__ = (
        'lineno',
        'tag',
    )


class UAdd(__ast.unaryop):
    """ UAdd """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class UnaryOp(__ast.expr):
    """ UnaryOp(unaryop op, expr operand) """
    def __init__(self, unaryop_op, expr_operand): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'op',
        'operand',
    )
    __match_args__ = (
        'op',
        'operand',
    )


class USub(__ast.unaryop):
    """ USub """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()
    __match_args__ = ()


class While(__ast.stmt):
    """ While(expr test, stmt* body, stmt* orelse) """
    def __init__(self, expr_test, stmt, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )
    __match_args__ = (
        'test',
        'body',
        'orelse',
    )


class With(__ast.stmt):
    """ With(withitem* items, stmt* body, string? type_comment) """
    def __init__(self, withitem, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    type_comment = None
    _fields = (
        'items',
        'body',
        'type_comment',
    )
    __match_args__ = (
        'items',
        'body',
        'type_comment',
    )


class withitem(__ast.AST):
    """ withitem(expr context_expr, expr? optional_vars) """
    def __init__(self, expr_context_expr, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    optional_vars = None
    _attributes = ()
    _fields = (
        'context_expr',
        'optional_vars',
    )
    __match_args__ = (
        'context_expr',
        'optional_vars',
    )


class Yield(__ast.expr):
    """ Yield(expr? value) """
    def __init__(self, expr, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    value = None
    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class YieldFrom(__ast.expr):
    """ YieldFrom(expr value) """
    def __init__(self, expr_value): # real signature unknown; restored from __doc__
        pass

    _fields = (
        'value',
    )
    __match_args__ = (
        'value',
    )


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x7f25fb60e8e0>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7f25fb60e980>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x7f25fb60ea20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7f25fb60eac0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7f25fb60eb60>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7f25fb60eca0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7f25fb60ede0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7f25fb60ef20>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7f25fb60dc60>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_ast', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

