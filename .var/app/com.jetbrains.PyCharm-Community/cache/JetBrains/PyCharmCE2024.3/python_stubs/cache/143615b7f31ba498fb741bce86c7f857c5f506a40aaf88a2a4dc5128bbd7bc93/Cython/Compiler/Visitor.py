# encoding: utf-8
# module Cython.Compiler.Visitor
# from /usr/lib/python3.11/site-packages/Cython/Compiler/Visitor.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import inspect as inspect # /usr/lib/python3.11/inspect.py
import Cython.Compiler.TypeSlots as TypeSlots # /usr/lib/python3.11/site-packages/Cython/Compiler/TypeSlots.py
import Cython.Compiler.Builtin as Builtin # /usr/lib/python3.11/site-packages/Cython/Compiler/Builtin.py
import Cython.Compiler.Nodes as Nodes # /usr/lib/python3.11/site-packages/Cython/Compiler/Nodes.py
import Cython.Compiler.ExprNodes as ExprNodes # /usr/lib/python3.11/site-packages/Cython/Compiler/ExprNodes.py
import Cython.Compiler.Errors as Errors # /usr/lib/python3.11/site-packages/Cython/Compiler/Errors.py
import Cython.Compiler.DebugFlags as DebugFlags # /usr/lib/python3.11/site-packages/Cython/Compiler/DebugFlags.py
import Cython.Compiler.Future as Future # /usr/lib/python3.11/site-packages/Cython/Compiler/Future.py

# functions

def find_special_method_for_binary_operator(*args, **kwargs): # real signature unknown
    """ Return the value for key if key is in the dictionary, else default. """
    pass

def find_special_method_for_unary_operator(*args, **kwargs): # real signature unknown
    """ Return the value for key if key is in the dictionary, else default. """
    pass

def recursively_replace_node(*args, **kwargs): # real signature unknown
    pass

def replace_node(*args, **kwargs): # real signature unknown
    """
    Replaces a node. ptr is of the form used on the access path stack
        (parent, attrname, listidx|None)
    """
    pass

def tree_contains(*args, **kwargs): # real signature unknown
    pass

# classes

class TreeVisitor(object):
    """
    Base class for writing visitors for a Cython tree, contains utilities for
        recursing such trees using visitors. Each node is
        expected to have a child_attrs iterable containing the names of attributes
        containing child nodes or lists of child nodes. Lists are not considered
        part of the tree structure (i.e. contained nodes are considered direct
        children of the parent node).
    
        visit_children visits each of the children of a given node (see the visit_children
        documentation). When recursing the tree using visit_children, an attribute
        access_path is maintained which gives information about the current location
        in the tree as a stack of tuples: (parent_node, attrname, index), representing
        the node, attribute and optional list index that was taken in each step in the path to
        the current node.
    
        Example:
    
        >>> class SampleNode(object):
        ...     child_attrs = ["head", "body"]
        ...     def __init__(self, value, head=None, body=None):
        ...         self.value = value
        ...         self.head = head
        ...         self.body = body
        ...     def __repr__(self): return "SampleNode(%s)" % self.value
        ...
        >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])
        >>> class MyVisitor(TreeVisitor):
        ...     def visit_SampleNode(self, node):
        ...         print("in %s %s" % (node.value, self.access_path))
        ...         self.visitchildren(node)
        ...         print("out %s" % node.value)
        ...
        >>> MyVisitor().visit(tree)
        in 0 []
        in 1 [(SampleNode(0), 'head', None)]
        out 1
        in 2 [(SampleNode(0), 'body', 0)]
        out 2
        in 3 [(SampleNode(0), 'body', 1)]
        out 3
        out 0
    """
    def dump_node(self, *args, **kwargs): # real signature unknown
        pass

    def visit(self, *args, **kwargs): # real signature unknown
        pass

    def visitchildren(self, *args, **kwargs): # real signature unknown
        pass

    def _find_node_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, value, head=None, body=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    access_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabeeb0>'


class VisitorTransform(TreeVisitor):
    """
    A tree transform is a base class for visitors that wants to do stream
        processing of the structure (rather than attributes etc.) of a tree.
    
        It implements __call__ to simply visit the argument node.
    
        It requires the visitor methods to return the nodes which should take
        the place of the visited node in the result tree (which can be the same
        or one or more replacement). Specifically, if the return value from
        a visitor method is:
    
        - [] or None; the visited node will be removed (set to None if an attribute and
        removed if in a list)
        - A single node; the visited node will be replaced by the returned node.
        - A list of nodes; the visited nodes will be replaced by all the nodes in the
        list. This will only work if the node was already a member of a list; if it
        was not, an exception will be raised. (Typically you want to ensure that you
        are within a StatListNode or similar before doing this.)
    """
    def recurse_to_children(self, *args, **kwargs): # real signature unknown
        pass

    def visitchildren(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabef10>'


class CythonTransform(VisitorTransform):
    """
    Certain common conventions and utilities for Cython transforms.
    
         - Sets up the context of the pipeline in self.context
         - Tracks directives in effect in self.current_directives
    """
    def visit_CompilerDirectivesNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_directives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabef70>'


class EnvTransform(CythonTransform):
    """ This transformation keeps a stack of the environments. """
    def current_env(self, *args, **kwargs): # real signature unknown
        pass

    def current_scope_node(self, *args, **kwargs): # real signature unknown
        pass

    def enter_scope(self, *args, **kwargs): # real signature unknown
        pass

    def exit_scope(self, *args, **kwargs): # real signature unknown
        pass

    def global_scope(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CArgDeclNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ClassDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CStructOrUnionDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FuncDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_GeneratorBodyDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ScopedExprNode(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    env_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabf030>'


class MethodDispatcherTransform(EnvTransform):
    """
    Base class for transformations that want to intercept on specific
        builtin functions or methods of builtin types, including special
        methods triggered by Python operators.  Must run after declaration
        analysis when entries were assigned.
    
        Naming pattern for handler methods is as follows:
    
        * builtin functions: _handle_(general|simple|any)_function_NAME
    
        * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME
    """
    def visit_BinopNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_GeneralCallNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PrimaryCmpNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SimpleCallNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_UnopNode(self, *args, **kwargs): # real signature unknown
        pass

    def _handle_function(self, *args, **kwargs): # real signature unknown
        """ Fallback handler """
        pass

    def _handle_method(self, *args, **kwargs): # real signature unknown
        """ Fallback handler """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabf090>'


class NodeFinder(TreeVisitor):
    """ Find out if a node appears in a subtree. """
    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    found = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabf150>'


class NodeRefCleanupMixin(object):
    """
    Clean up references to nodes that were replaced.
    
        NOTE: this implementation assumes that the replacement is
        done first, before hitting any further references during
        normal tree traversal.  This needs to be arranged by calling
        "self.visitchildren()" at a proper place in the transform
        and by ordering the "child_attrs" of nodes appropriately.
    """
    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CloneNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ResultRefNode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'Cython.Compiler.Visitor\', \'__doc__\': \'\\n    Clean up references to nodes that were replaced.\\n\\n    NOTE: this implementation assumes that the replacement is\\n    done first, before hitting any further references during\\n    normal tree traversal.  This needs to be arranged by calling\\n    "self.visitchildren()" at a proper place in the transform\\n    and by ordering the "child_attrs" of nodes appropriately.\\n    \', \'__init__\': <cyfunction NodeRefCleanupMixin.__init__ at 0x7f25fa1f8fb0>, \'visit_CloneNode\': <cyfunction NodeRefCleanupMixin.visit_CloneNode at 0x7f25fa1f9080>, \'visit_ResultRefNode\': <cyfunction NodeRefCleanupMixin.visit_ResultRefNode at 0x7f25fa1f9150>, \'replace\': <cyfunction NodeRefCleanupMixin.replace at 0x7f25fa1f92f0>, \'__dict__\': <attribute \'__dict__\' of \'NodeRefCleanupMixin\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'NodeRefCleanupMixin\' objects>})'


class PrintTree(TreeVisitor):
    """
    Prints a representation of the tree to standard output.
        Subclass and override repr_of to provide more information
        about nodes.
    """
    def indent(self, *args, **kwargs): # real signature unknown
        pass

    def repr_of(self, *args, **kwargs): # real signature unknown
        pass

    def unindent(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CloneNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def _print_node(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.Visitor', '__doc__': 'Prints a representation of the tree to standard output.\\n    Subclass and override repr_of to provide more information\\n    about nodes. ', '__init__': <cyfunction PrintTree.__init__ at 0x7f25fa1f9e50>, 'indent': <cyfunction PrintTree.indent at 0x7f25fa1f9f20>, 'unindent': <cyfunction PrintTree.unindent at 0x7f25fa1f9ff0>, '__call__': <cyfunction PrintTree.__call__ at 0x7f25fa1fa190>, 'visit_Node': <cyfunction PrintTree.visit_Node at 0x7f25fa1fa260>, 'visit_CloneNode': <cyfunction PrintTree.visit_CloneNode at 0x7f25fa1fa330>, '_print_node': <cyfunction PrintTree._print_node at 0x7f25fa1fa400>, 'repr_of': <cyfunction PrintTree.repr_of at 0x7f25fa1fa4d0>, '__dict__': <attribute '__dict__' of 'PrintTree' objects>, '__weakref__': <attribute '__weakref__' of 'PrintTree' objects>})"


class RecursiveNodeReplacer(VisitorTransform):
    """
    Recursively replace all occurrences of a node in a subtree by
        another node.
    """
    def visit_CloneNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    new_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabf0f0>'


class ScopeTrackingTransform(CythonTransform):
    # no doc
    def visit_CClassDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CStructOrUnionDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FuncDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ModuleNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PyClassDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    scope_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25faabefd0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faaceed0>'

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Compiler.Visitor', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faaceed0>, origin='/usr/lib/python3.11/site-packages/Cython/Compiler/Visitor.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

