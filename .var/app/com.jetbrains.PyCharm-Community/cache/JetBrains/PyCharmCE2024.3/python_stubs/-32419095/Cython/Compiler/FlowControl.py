# encoding: utf-8
# module Cython.Compiler.FlowControl
# from /usr/lib/python3.11/site-packages/Cython/Compiler/FlowControl.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import Cython.Compiler.Options as Options # /usr/lib/python3.11/site-packages/Cython/Compiler/Options.py
import Cython.Compiler.ParseTreeTransforms as __Cython_Compiler_ParseTreeTransforms
import Cython.Compiler.Visitor as __Cython_Compiler_Visitor


# functions

def __pyx_unpickle_AssignmentCollector(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_AssignmentList(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlBlock(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlFlow(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlFlowAnalysis(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ExitBlock(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MessageCollection(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_NameAssignment(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uninitialized(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Unknown(*args, **kwargs): # real signature unknown
    pass

# classes

class NameAssignment(object):
    # no doc
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def type_dependencies(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inferred_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_arg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_deletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lhs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rhs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Argument(NameAssignment):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__init__': <cyfunction Argument.__init__ at 0x7f25fa070790>, '__dict__': <attribute '__dict__' of 'Argument' objects>, '__weakref__': <attribute '__weakref__' of 'Argument' objects>, '__doc__': None})"


class AssignmentCollector(__Cython_Compiler_Visitor.TreeVisitor):
    # no doc
    def visit_CascadedAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SingleAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa8890e0>'


class AssignmentList(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConstantFolding(__Cython_Compiler_Visitor.VisitorTransform, __Cython_Compiler_ParseTreeTransforms.SkipDeclarations):
    """
    Calculate the result of constant expressions to store it in
        ``expr_node.constant_result``, and replace trivial cases by their
        constant result.
    
        General rules:
    
        - We calculate float constants to make them available to the
          compiler, but we do not aggregate them into a single literal
          node to prevent any loss of precision.
    
        - We recursively calculate constants from non-literal nodes to
          make them available to the compiler, but we only aggregate
          literal nodes at each step.  Non-literal nodes are never merged
          into a single node.
    """
    def visit_AddNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_BinopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_BoolBinopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ComprehensionNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_CondExprNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ExprNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ExprStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ForInStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_FormattedValueNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_IfStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_JoinedStrNode(self, node): # reliably restored by inspect
        """
        Clean up after the parser by discarding empty Unicode strings and merging
                substring sequences.  Empty or single-value join lists are not uncommon
                because f-string format specs are always parsed into JoinedStrNodes.
        """
        pass

    def visit_MergedDictNode(self, node): # reliably restored by inspect
        """ Unpack **args in place if we can. """
        pass

    def visit_MergedSequenceNode(self, node): # reliably restored by inspect
        """ Unpack *args in place if we can. """
        pass

    def visit_ModNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_MulNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PrimaryCmpNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_SequenceNode(self, node): # reliably restored by inspect
        """ Unpack *args in place if we can. """
        pass

    def visit_SliceIndexNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_UnopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_WhileStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _bool_node(self, node, value): # reliably restored by inspect
        # no doc
        pass

    def _build_fstring(self, pos, ustring, format_args): # reliably restored by inspect
        # no doc
        pass

    def _calculate_const(self, node): # reliably restored by inspect
        # no doc
        pass

    def _calculate_constant_seq(self, node, sequence_node, factor): # reliably restored by inspect
        # no doc
        pass

    def _handle_NotNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _handle_UnaryMinusNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _handle_UnaryPlusNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _multiply_string(self, node, string_node, multiplier_node): # reliably restored by inspect
        # no doc
        pass

    def _negate_operator(self, *args, **kwargs): # real signature unknown
        """ Return the value for key if key is in the dictionary, else default. """
        pass

    def _widest_node_class(self, *nodes): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, reevaluate=False): # reliably restored by inspect
        """
        The reevaluate argument specifies whether constant values that were
                previously computed should be recomputed.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    NODE_TYPE_ORDER = [
        None, # (!) real value is "<class 'Cython.Compiler.ExprNodes.BoolNode'>"
        None, # (!) real value is "<class 'Cython.Compiler.ExprNodes.CharNode'>"
        None, # (!) real value is "<class 'Cython.Compiler.ExprNodes.IntNode'>"
        None, # (!) real value is "<class 'Cython.Compiler.ExprNodes.FloatNode'>"
    ]
    _parse_string_format_regex = '(%(?:(?:[-0-9]+|[ ])?(?:[.][0-9]+)?)?.)'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.Optimize', '__doc__': 'Calculate the result of constant expressions to store it in\\n    ``expr_node.constant_result``, and replace trivial cases by their\\n    constant result.\\n\\n    General rules:\\n\\n    - We calculate float constants to make them available to the\\n      compiler, but we do not aggregate them into a single literal\\n      node to prevent any loss of precision.\\n\\n    - We recursively calculate constants from non-literal nodes to\\n      make them available to the compiler, but we only aggregate\\n      literal nodes at each step.  Non-literal nodes are never merged\\n      into a single node.\\n    ', '__init__': <function ConstantFolding.__init__ at 0x7f25fa09ad40>, '_calculate_const': <function ConstantFolding._calculate_const at 0x7f25fa09ade0>, 'NODE_TYPE_ORDER': [<class 'Cython.Compiler.ExprNodes.BoolNode'>, <class 'Cython.Compiler.ExprNodes.CharNode'>, <class 'Cython.Compiler.ExprNodes.IntNode'>, <class 'Cython.Compiler.ExprNodes.FloatNode'>], '_widest_node_class': <function ConstantFolding._widest_node_class at 0x7f25fa09ae80>, '_bool_node': <function ConstantFolding._bool_node at 0x7f25fa09af20>, 'visit_ExprNode': <function ConstantFolding.visit_ExprNode at 0x7f25fa09afc0>, 'visit_UnopNode': <function ConstantFolding.visit_UnopNode at 0x7f25fa09b060>, '_negate_operator': <built-in method get of dict object at 0x7f25fa19b600>, '_handle_NotNode': <function ConstantFolding._handle_NotNode at 0x7f25fa09b100>, '_handle_UnaryMinusNode': <function ConstantFolding._handle_UnaryMinusNode at 0x7f25fa09b1a0>, '_handle_UnaryPlusNode': <function ConstantFolding._handle_UnaryPlusNode at 0x7f25fa09b240>, 'visit_BoolBinopNode': <function ConstantFolding.visit_BoolBinopNode at 0x7f25fa09b2e0>, 'visit_BinopNode': <function ConstantFolding.visit_BinopNode at 0x7f25fa09b380>, 'visit_AddNode': <function ConstantFolding.visit_AddNode at 0x7f25fa09b420>, 'visit_MulNode': <function ConstantFolding.visit_MulNode at 0x7f25fa09b4c0>, '_multiply_string': <function ConstantFolding._multiply_string at 0x7f25fa09b560>, '_calculate_constant_seq': <function ConstantFolding._calculate_constant_seq at 0x7f25fa09b600>, 'visit_ModNode': <function ConstantFolding.visit_ModNode at 0x7f25fa09b6a0>, '_parse_string_format_regex': '(%(?:(?:[-0-9]+|[ ])?(?:[.][0-9]+)?)?.)', '_build_fstring': <function ConstantFolding._build_fstring at 0x7f25fa09b740>, 'visit_FormattedValueNode': <function ConstantFolding.visit_FormattedValueNode at 0x7f25fa09b7e0>, 'visit_JoinedStrNode': <function ConstantFolding.visit_JoinedStrNode at 0x7f25fa09b880>, 'visit_MergedDictNode': <function ConstantFolding.visit_MergedDictNode at 0x7f25fa09b920>, 'visit_MergedSequenceNode': <function ConstantFolding.visit_MergedSequenceNode at 0x7f25fa09b9c0>, 'visit_SequenceNode': <function ConstantFolding.visit_SequenceNode at 0x7f25fa09ba60>, 'visit_PrimaryCmpNode': <function ConstantFolding.visit_PrimaryCmpNode at 0x7f25fa09bb00>, 'visit_CondExprNode': <function ConstantFolding.visit_CondExprNode at 0x7f25fa09bba0>, 'visit_IfStatNode': <function ConstantFolding.visit_IfStatNode at 0x7f25fa09bc40>, 'visit_SliceIndexNode': <function ConstantFolding.visit_SliceIndexNode at 0x7f25fa09bce0>, 'visit_ComprehensionNode': <function ConstantFolding.visit_ComprehensionNode at 0x7f25fa09bd80>, 'visit_ForInStatNode': <function ConstantFolding.visit_ForInStatNode at 0x7f25fa09be20>, 'visit_WhileStatNode': <function ConstantFolding.visit_WhileStatNode at 0x7f25fa09bec0>, 'visit_ExprStatNode': <function ConstantFolding.visit_ExprStatNode at 0x7f25fa09bf60>, 'visit_Node': <cyfunction VisitorTransform.recurse_to_children at 0x7f25fa6031d0>, '__dict__': <attribute '__dict__' of 'ConstantFolding' objects>, '__weakref__': <attribute '__weakref__' of 'ConstantFolding' objects>})"


class ControlBlock(object):
    """
    Control flow graph node. Sequence of assignments and name references.
    
           children  set of children nodes
           parents   set of parent nodes
           positions set of position markers
    
           stats     list of block statements
           gen       dict of assignments generated by this block
           bounded   set  of entries that are definitely bounded in this block
    
           Example:
    
            a = 1
            b = a + c # 'c' is already bounded or exception here
    
            stats = [Assignment(a), NameReference(a), NameReference(c),
                         Assignment(b)]
            gen = {Entry(a): Assignment(a), Entry(b): Assignment(b)}
            bounded = set([Entry(a), Entry(c)])
    """
    def add_child(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        """ Detach block from parents and children. """
        pass

    def empty(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    bounded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_kill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa888060>'


class ControlFlow(object):
    """
    Control-flow graph.
    
           entry_point ControlBlock entry point for this graph
           exit_point  ControlBlock normal exit point
           block       ControlBlock current block
           blocks      set    children nodes
           entries     set    tracked entries
           loops       list   stack for loop descriptors
           exceptions  list   stack for exception descriptors
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        """ Set initial state, map assignments to bits. """
        pass

    def is_statically_assigned(self, *args, **kwargs): # real signature unknown
        pass

    def is_tracked(self, *args, **kwargs): # real signature unknown
        pass

    def map_one(self, *args, **kwargs): # real signature unknown
        pass

    def mark_argument(self, *args, **kwargs): # real signature unknown
        pass

    def mark_assignment(self, *args, **kwargs): # real signature unknown
        pass

    def mark_deletion(self, *args, **kwargs): # real signature unknown
        pass

    def mark_position(self, *args, **kwargs): # real signature unknown
        """ Mark position, will be used to draw graph nodes. """
        pass

    def mark_reference(self, *args, **kwargs): # real signature unknown
        pass

    def newblock(self, *args, **kwargs): # real signature unknown
        """
        Create floating block linked to `parent` if given.
        
                   NOTE: Block is NOT added to self.blocks
        """
        pass

    def nextblock(self, *args, **kwargs): # real signature unknown
        """
        Create block children block linked to current or `parent` if given.
        
                   NOTE: Block is added to self.blocks
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """ Delete unreachable and orphan blocks. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    assmts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    block = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entry_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exit_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa589c80>'


class ControlFlowAnalysis(__Cython_Compiler_Visitor.CythonTransform):
    # no doc
    def mark_assignment(self, *args, **kwargs): # real signature unknown
        pass

    def mark_forloop_target(self, *args, **kwargs): # real signature unknown
        pass

    def mark_position(self, *args, **kwargs): # real signature unknown
        """ Mark position if DOT output is enabled. """
        pass

    def visit_AmpersandNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_AssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_AsyncForStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_BreakStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CArgDeclNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CascadedAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ComprehensionNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ContinueStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CTypeDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_DefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_DelStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ForFromStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ForInStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FromImportStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FuncDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_GeneratorBodyDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_IfStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_InPlaceAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_LoopNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ModuleNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_NameNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelRangeNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelWithBlockNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PyClassDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_RaiseStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ReraiseStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ReturnStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ScopedExprNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SingleAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SizeofVarNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_StatListNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_TryExceptStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_TryFinallyStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_TypeidNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WhileStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WithStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WithTargetAssignmentStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def _delete_privates(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa5df630>'


class ControlFlowState(list):
    # no doc
    def one(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    cf_is_null = False
    cf_maybe_null = False
    is_single = False
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', 'cf_maybe_null': False, 'cf_is_null': False, 'is_single': False, '__init__': <cyfunction ControlFlowState.__init__ at 0x7f25fa071220>, 'one': <cyfunction ControlFlowState.one at 0x7f25fa0713c0>, '__dict__': <attribute '__dict__' of 'ControlFlowState' objects>, '__weakref__': <attribute '__weakref__' of 'ControlFlowState' objects>, '__doc__': None})"


class ExceptionDescr(object):
    """
    Exception handling helper.
    
        entry_point   ControlBlock Exception handling entry point
        finally_enter ControlBlock Normal finally clause entry point
        finally_exit  ControlBlock Normal finally clause exit point
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__doc__': 'Exception handling helper.\\n\\n    entry_point   ControlBlock Exception handling entry point\\n    finally_enter ControlBlock Normal finally clause entry point\\n    finally_exit  ControlBlock Normal finally clause exit point\\n    ', '__init__': <cyfunction ExceptionDescr.__init__ at 0x7f25fa070040>, '__dict__': <attribute '__dict__' of 'ExceptionDescr' objects>, '__weakref__': <attribute '__weakref__' of 'ExceptionDescr' objects>})"


class ExitBlock(ControlBlock):
    """ Non-empty exit point block. """
    def empty(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25fa8880c0>'


class GV(object):
    """ Graphviz DOT renderer. """
    def render(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__doc__': 'Graphviz DOT renderer.', '__init__': <cyfunction GV.__init__ at 0x7f25fa071700>, 'render': <cyfunction GV.render at 0x7f25fa071a40>, '__dict__': <attribute '__dict__' of 'GV' objects>, '__weakref__': <attribute '__weakref__' of 'GV' objects>})"


class GVContext(object):
    """ Graphviz subgraph object. """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def escape(self, *args, **kwargs): # real signature unknown
        pass

    def extract_sources(self, *args, **kwargs): # real signature unknown
        pass

    def nodeid(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        """ Render graphviz dot graph """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__doc__': 'Graphviz subgraph object.', '__init__': <cyfunction GVContext.__init__ at 0x7f25fa0712f0>, 'add': <cyfunction GVContext.add at 0x7f25fa071560>, 'nodeid': <cyfunction GVContext.nodeid at 0x7f25fa071630>, 'extract_sources': <cyfunction GVContext.extract_sources at 0x7f25fa0717d0>, 'render': <cyfunction GVContext.render at 0x7f25fa0718a0>, 'escape': <cyfunction GVContext.escape at 0x7f25fa071970>, '__dict__': <attribute '__dict__' of 'GVContext' objects>, '__weakref__': <attribute '__weakref__' of 'GVContext' objects>})"


class LoopDescr(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__init__': <cyfunction LoopDescr.__init__ at 0x7f25f9dcfe00>, '__dict__': <attribute '__dict__' of 'LoopDescr' objects>, '__weakref__': <attribute '__weakref__' of 'LoopDescr' objects>, '__doc__': None})"


class MessageCollection(object):
    """ Collect error/warnings messages first then sort """
    def error(self, *args, **kwargs): # real signature unknown
        pass

    def report(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class NameDeletion(NameAssignment):
    # no doc
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__init__': <cyfunction NameDeletion.__init__ at 0x7f25fa070a00>, 'infer_type': <cyfunction NameDeletion.infer_type at 0x7f25fa070ad0>, '__dict__': <attribute '__dict__' of 'NameDeletion' objects>, '__weakref__': <attribute '__weakref__' of 'NameDeletion' objects>, '__doc__': None})"


class NameReference(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__init__': <cyfunction NameReference.__init__ at 0x7f25fa070fb0>, '__repr__': <cyfunction NameReference.__repr__ at 0x7f25fa071080>, '__dict__': <attribute '__dict__' of 'NameReference' objects>, '__weakref__': <attribute '__weakref__' of 'NameReference' objects>, '__doc__': None})"


class StaticAssignment(NameAssignment):
    """ Initialised at declaration time, e.g. stack allocation. """
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def type_dependencies(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Compiler.FlowControl', '__doc__': 'Initialised at declaration time, e.g. stack allocation.', '__init__': <cyfunction StaticAssignment.__init__ at 0x7f25fa070520>, 'infer_type': <cyfunction StaticAssignment.infer_type at 0x7f25fa0705f0>, 'type_dependencies': <cyfunction StaticAssignment.type_dependencies at 0x7f25fa0706c0>, '__dict__': <attribute '__dict__' of 'StaticAssignment' objects>, '__weakref__': <attribute '__weakref__' of 'StaticAssignment' objects>})"


class Uninitialized(object):
    """ Definitely not initialised yet. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class Unknown(object):
    """ Coming from outer closure, might be initialised or not. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faaced50>'

__pyx_capi__ = {
    'check_definitions': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6Cython_8Compiler_11FlowControl_ControlFlow *, PyObject *)" at 0x7f25fa888030>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Compiler.FlowControl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faaced50>, origin='/usr/lib/python3.11/site-packages/Cython/Compiler/FlowControl.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

