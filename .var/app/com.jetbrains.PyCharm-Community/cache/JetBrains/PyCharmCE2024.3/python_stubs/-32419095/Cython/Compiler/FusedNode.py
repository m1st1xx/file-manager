# encoding: utf-8
# module Cython.Compiler.FusedNode
# from /usr/lib/python3.11/site-packages/Cython/Compiler/FusedNode.cpython-311-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import copy as copy # /usr/lib/python3.11/copy.py
import Cython.Compiler.ExprNodes as ExprNodes # /usr/lib/python3.11/site-packages/Cython/Compiler/ExprNodes.py
import Cython.Compiler.PyrexTypes as PyrexTypes # /usr/lib/python3.11/site-packages/Cython/Compiler/PyrexTypes.py
import Cython.Compiler.MemoryView as MemoryView # /usr/lib/python3.11/site-packages/Cython/Compiler/MemoryView.py
import Cython.Compiler.ParseTreeTransforms as ParseTreeTransforms # /usr/lib/python3.11/site-packages/Cython/Compiler/ParseTreeTransforms.py
import Cython.Compiler.StringEncoding as StringEncoding # /usr/lib/python3.11/site-packages/Cython/Compiler/StringEncoding.py
import Cython.Compiler.Errors as Errors # /usr/lib/python3.11/site-packages/Cython/Compiler/Errors.py
import Cython.Compiler.ExprNodes as __Cython_Compiler_ExprNodes
import Cython.Compiler.Nodes as __Cython_Compiler_Nodes


# no functions
# classes

class FuncDefNode(__Cython_Compiler_Nodes.StatNode, __Cython_Compiler_Nodes.BlockNode):
    # no doc
    def align_argument_type(self, env, arg): # reliably restored by inspect
        # no doc
        pass

    def analyse_annotation(self, env, annotation): # reliably restored by inspect
        # no doc
        pass

    def analyse_annotations(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_default_values(self, env): # reliably restored by inspect
        # no doc
        pass

    def create_local_scope(self, env): # reliably restored by inspect
        # no doc
        pass

    def declare_argument(self, env, arg): # reliably restored by inspect
        # no doc
        pass

    def generate_arg_none_check(self, arg, code): # reliably restored by inspect
        # no doc
        pass

    def generate_arg_type_test(self, arg, code): # reliably restored by inspect
        # no doc
        pass

    def generate_execution_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_body(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_definitions(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_wrapper_functions(self, code): # reliably restored by inspect
        # no doc
        pass

    def getbuffer_check(self, code): # reliably restored by inspect
        # no doc
        pass

    def getbuffer_error_cleanup(self, code): # reliably restored by inspect
        # no doc
        pass

    def getbuffer_init(self, code): # reliably restored by inspect
        # no doc
        pass

    def getbuffer_normal_cleanup(self, code): # reliably restored by inspect
        # no doc
        pass

    def get_preprocessor_guard(self): # reliably restored by inspect
        # no doc
        pass

    def need_gil_acquisition(self, lenv): # reliably restored by inspect
        # no doc
        pass

    def _get_py_buffer_info(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, pos, **kw): # reliably restored by inspect
        # no doc
        pass

    code_object = None
    has_fused_arguments = False
    is_async_def = False
    is_cyfunction = False
    is_generator = False
    is_generator_body = False
    modifiers = []
    needs_closure = False
    needs_outer_scope = False
    pymethdef_required = False
    py_func = None
    starstar_arg = None
    star_arg = None


class CFuncDefNode(__Cython_Compiler_Nodes.FuncDefNode):
    # no doc
    def analyse_declarations(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_expressions(self, env): # reliably restored by inspect
        # no doc
        pass

    def caller_will_check_exceptions(self): # reliably restored by inspect
        # no doc
        pass

    def call_self_node(self, omit_optional_args=0, is_module_scope=0): # reliably restored by inspect
        # no doc
        pass

    def declare_arguments(self, env): # reliably restored by inspect
        # no doc
        pass

    def declare_cpdef_wrapper(self, env): # reliably restored by inspect
        # no doc
        pass

    def error_value(self): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_conversion_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_declarations(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_parsing_code(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_type_tests(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_execution_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_header(self, code, with_pymethdef, with_opt_args=1, with_dispatch=1, cname=None): # reliably restored by inspect
        # no doc
        pass

    def generate_keyword_list(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_wrapper_functions(self, code): # reliably restored by inspect
        # no doc
        pass

    def needs_assignment_synthesis(self, env, code=None): # reliably restored by inspect
        # no doc
        pass

    def need_gil_acquisition(self, lenv): # reliably restored by inspect
        # no doc
        pass

    def nogil_check(self, env): # reliably restored by inspect
        # no doc
        pass

    def unqualified_name(self): # reliably restored by inspect
        # no doc
        pass

    def _validate_type_visibility(self, type, pos, env): # reliably restored by inspect
        """
        Ensure that types used in cdef functions are public or api, or
                defined in a C header.
        """
        pass

    def __init__(self, pos, **kw): # reliably restored by inspect
        # no doc
        pass

    code_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    child_attrs = [
        'base_type',
        'declarator',
        'body',
        'py_func_stat',
    ]
    decorators = None
    directive_locals = None
    directive_returns = None
    inline_in_pxd = False
    is_const_method = False
    override = None
    py_func_stat = None
    template_declaration = None


class CloneNode(__Cython_Compiler_ExprNodes.CoercionNode):
    # no doc
    def analyse_types(self, env): # reliably restored by inspect
        # no doc
        pass

    def coerce_to(self, dest_type, env): # reliably restored by inspect
        # no doc
        pass

    def free_temps(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_disposal_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_evaluation_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_result_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def infer_type(self, env): # reliably restored by inspect
        # no doc
        pass

    def is_simple(self): # reliably restored by inspect
        # no doc
        pass

    def may_be_none(self): # reliably restored by inspect
        # no doc
        pass

    def result(self): # reliably restored by inspect
        # no doc
        pass

    def type_dependencies(self, env): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg): # reliably restored by inspect
        # no doc
        pass

    nogil_check = None
    subexprs = []


class DefNode(__Cython_Compiler_Nodes.FuncDefNode):
    # no doc
    def analyse_argument_types(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_declarations(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_expressions(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_signature(self, env): # reliably restored by inspect
        # no doc
        pass

    def as_cfunction(self, cfunc=None, scope=None, overridable=True, returns=None, except_val=None, modifiers=None, nogil=False, with_gil=False): # reliably restored by inspect
        # no doc
        pass

    def bad_signature(self): # reliably restored by inspect
        # no doc
        pass

    def caller_will_check_exceptions(self): # reliably restored by inspect
        # no doc
        pass

    def declare_arguments(self, env): # reliably restored by inspect
        # no doc
        pass

    def declare_lambda_function(self, env): # reliably restored by inspect
        # no doc
        pass

    def declare_pyfunction(self, env): # reliably restored by inspect
        # no doc
        pass

    def declare_python_arg(self, env, arg): # reliably restored by inspect
        # no doc
        pass

    def error_value(self): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_declarations(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_parsing_code(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_argument_type_tests(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_definitions(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_header(self, code, with_pymethdef, proto_only=0): # reliably restored by inspect
        # no doc
        pass

    def generate_keyword_list(self, code): # reliably restored by inspect
        # no doc
        pass

    def is_cdef_func_compatible(self): # reliably restored by inspect
        """
        Determines if the function's signature is compatible with a
                cdef function.  This can be used before calling
                .as_cfunction() to see if that will be successful.
        """
        pass

    def needs_assignment_synthesis(self, env, code=None): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, pos, **kwds): # reliably restored by inspect
        # no doc
        pass

    acquire_gil = 0
    child_attrs = [
        'args',
        'star_arg',
        'starstar_arg',
        'body',
        'decorators',
        'return_type_annotation',
    ]
    decorators = None
    defaults_getter = None
    defaults_struct = None
    doc = None
    entry = None
    func_cname = None
    fused_py_func = False
    is_classmethod = False
    is_staticmethod = False
    is_wrapper = 0
    lambda_name = None
    no_assignment_synthesis = 0
    outer_attrs = [
        'decorators',
        'return_type_annotation',
    ]
    py_cfunc_node = None
    py_wrapper = None
    py_wrapper_required = True
    reqd_kw_flags_cname = '0'
    requires_classobj = False
    return_type_annotation = None
    self_in_stararg = 0
    specialized_cpdefs = None


class StatListNode(__Cython_Compiler_Nodes.Node):
    # no doc
    def analyse_declarations(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_expressions(self, env): # reliably restored by inspect
        # no doc
        pass

    def annotate(self, code): # reliably restored by inspect
        # no doc
        pass

    def create_analysed(pos, env, *args, **kw): # reliably restored by inspect
        # no doc
        pass

    def generate_execution_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_function_definitions(self, env, code): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, pos, **kw): # reliably restored by inspect
        # no doc
        pass

    child_attrs = [
        'stats',
    ]


class FusedCFuncDefNode(__Cython_Compiler_Nodes.StatListNode):
    """
    This node replaces a function with fused arguments. It deep-copies the
        function for every permutation of fused types, and allocates a new local
        scope for it. It keeps track of the original function in self.node, and
        the entry of the original function in the symbol table is given the
        'fused_cfunction' attribute which points back to us.
        Then when a function lookup occurs (to e.g. call it), the call can be
        dispatched to the right function.
    
        node    FuncDefNode    the original function
        nodes   [FuncDefNode]  list of copies of node with different specific types
        py_func DefNode        the fused python function subscriptable from
                               Python space
        __signatures__         A DictNode mapping signature specialization strings
                               to PyCFunction nodes
        resulting_fused_function  PyCFunction for the fused DefNode that delegates
                                  to specializations
        fused_func_assignment   Assignment of the fused function to the function name
        defaults_tuple          TupleNode of defaults (letting PyCFunctionNode build
                                defaults would result in many different tuples)
        specialized_pycfuncs    List of synthesized pycfunction nodes for the
                                specializations
        code_object             CodeObjectNode shared by all specializations and the
                                fused function
    
        fused_compound_types    All fused (compound) types (e.g. floating[:])
    """
    def analyse_expressions(self, *args, **kwargs): # real signature unknown
        """
        Analyse the expressions. Take care to only evaluate default arguments
                once and clone the result for all specializations
        """
        pass

    def annotate(self, *args, **kwargs): # real signature unknown
        pass

    def copy_cdef(self, *args, **kwargs): # real signature unknown
        """
        Create a copy of the original c(p)def function for all specialized
                versions.
        """
        pass

    def copy_def(self, *args, **kwargs): # real signature unknown
        """
        Create a copy of the original def or lambda function for specialized
                versions.
        """
        pass

    def create_new_local_scope(self, *args, **kwargs): # real signature unknown
        """
        Create a new local scope for the copied node and append it to
                self.nodes. A new local scope is needed because the arguments with the
                fused types are already in the local scope, and we need the specialized
                entries created after analyse_declarations on each specialized version
                of the (CFunc)DefNode.
                f2s is a dict mapping each fused type to its specialized version
        """
        pass

    def generate_execution_code(self, *args, **kwargs): # real signature unknown
        pass

    def generate_function_definitions(self, *args, **kwargs): # real signature unknown
        pass

    def make_fused_cpdef(self, *args, **kwargs): # real signature unknown
        """
        This creates the function that is indexable from Python and does
                runtime dispatch based on the argument types. The function gets the
                arg tuple and kwargs dict (or None) and the defaults tuple
                as arguments from the Binding Fused Function's tp_call.
        """
        pass

    def replace_fused_typechecks(self, *args, **kwargs): # real signature unknown
        """
        Branch-prune fused type checks like
        
                    if fused_t is int:
                        ...
        
                Returns whether an error was issued and whether we should stop in
                in order to prevent a flood of errors.
        """
        pass

    def specialize_copied_def(self, *args, **kwargs): # real signature unknown
        """
        Specialize the copy of a DefNode given the copied node,
                the specialization cname and the original DefNode entry
        """
        pass

    def synthesize_defnodes(self, *args, **kwargs): # real signature unknown
        """ Create the __signatures__ dict of PyCFunctionNode specializations. """
        pass

    def update_fused_defnode_entry(self, *args, **kwargs): # real signature unknown
        pass

    def _buffer_checks(self, *args, **kwargs): # real signature unknown
        """
        Generate Cython code to match objects to buffer specializations.
                First try to get a numpy dtype object and match it against the individual
                specializations. If that fails, try naively to coerce the object
                to each specialization, which obtains the buffer each time and tries
                to match the format string.
        """
        pass

    def _buffer_check_numpy_dtype(self, *args, **kwargs): # real signature unknown
        """ Match a numpy dtype object to the individual specializations. """
        pass

    def _buffer_check_numpy_dtype_setup_cases(self, *args, **kwargs): # real signature unknown
        """ Setup some common cases to match dtypes against specializations """
        pass

    def _buffer_declarations(self, *args, **kwargs): # real signature unknown
        """
        If we have any buffer specializations, write out some variable
                declarations and imports.
        """
        pass

    def _buffer_parse_format_string_check(self, *args, **kwargs): # real signature unknown
        """
        For each specialized type, try to coerce the object to a memoryview
                slice of that type. This means obtaining a buffer and parsing the
                format string.
                TODO: separate buffer acquisition from format parsing
        """
        pass

    def _dtype_name(self, *args, **kwargs): # real signature unknown
        pass

    def _dtype_type(self, *args, **kwargs): # real signature unknown
        pass

    def _fused_instance_checks(self, *args, **kwargs): # real signature unknown
        """
        Generate Cython code for instance checks, matching an object to
                specialized types.
        """
        pass

    def _get_fused_base_types(self, *args, **kwargs): # real signature unknown
        """
        Get a list of unique basic fused types, from a list of
                (possibly) compound fused types.
        """
        pass

    def _sizeof_dtype(self, *args, **kwargs): # real signature unknown
        pass

    def _specialize_function_args(self, *args, **kwargs): # real signature unknown
        pass

    def _split_fused_types(self, *args, **kwargs): # real signature unknown
        """ Specialize fused types and split into normal types and buffer types. """
        pass

    def _unpack_argument(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    child_attrs = [
        'stats',
        '__signatures__',
        'resulting_fused_function',
        'fused_func_assignment',
    ]
    decorators = None
    defaults_tuple = None
    fused_func_assignment = None
    match = "dest_sig[{{dest_sig_idx}}] = '{{specialized_type_name}}'"
    no_match = 'dest_sig[{{dest_sig_idx}}] = None'
    resulting_fused_function = None
    __signatures__ = None


class OrderedSet(object):
    # no doc
    def add(self, e): # reliably restored by inspect
        # no doc
        pass

    def update(self, elements): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, elements='()'): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'Cython.Utils', '__init__': <function OrderedSet.__init__ at 0x7f25fa600400>, '__iter__': <function OrderedSet.__iter__ at 0x7f25fa6004a0>, 'update': <function OrderedSet.update at 0x7f25fa600540>, 'add': <function OrderedSet.add at 0x7f25fa6005e0>, '__dict__': <attribute '__dict__' of 'OrderedSet' objects>, '__weakref__': <attribute '__weakref__' of 'OrderedSet' objects>, '__doc__': None})"


class ProxyNode(__Cython_Compiler_ExprNodes.CoercionNode):
    """
    A node that should not be replaced by transforms or other means,
        and hence can be useful to wrap the argument to a clone node
    
        MyNode    -> ProxyNode -> ArgNode
        CloneNode -^
    """
    def analyse_types(self, env): # reliably restored by inspect
        # no doc
        pass

    def free_temps(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_disposal_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_evaluation_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def generate_result_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def infer_type(self, env): # reliably restored by inspect
        # no doc
        pass

    def is_simple(self): # reliably restored by inspect
        # no doc
        pass

    def may_be_none(self): # reliably restored by inspect
        # no doc
        pass

    def result(self): # reliably restored by inspect
        # no doc
        pass

    def _proxy_type(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg): # reliably restored by inspect
        # no doc
        pass

    nogil_check = None


class TupleNode(__Cython_Compiler_ExprNodes.SequenceNode):
    # no doc
    def analyse_as_type(self, env): # reliably restored by inspect
        # no doc
        pass

    def analyse_types(self, env, skip_children=False): # reliably restored by inspect
        # no doc
        pass

    def as_list(self): # reliably restored by inspect
        # no doc
        pass

    def calculate_constant_result(self): # reliably restored by inspect
        # no doc
        pass

    def calculate_result_code(self): # reliably restored by inspect
        # no doc
        pass

    def coerce_to(self, dst_type, env): # reliably restored by inspect
        # no doc
        pass

    def compile_time_value(self, denv): # reliably restored by inspect
        # no doc
        pass

    def generate_operation_code(self, code): # reliably restored by inspect
        # no doc
        pass

    def infer_type(self, env): # reliably restored by inspect
        # no doc
        pass

    def is_simple(self): # reliably restored by inspect
        # no doc
        pass

    def nonlocally_immutable(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, pos, **kw): # reliably restored by inspect
        # no doc
        pass

    gil_message = 'Constructing Python tuple'
    is_partly_literal = False
    type = ExprNodes.tuple_type


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacedd0>'

__spec__ = None # (!) real value is "ModuleSpec(name='Cython.Compiler.FusedNode', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25faacedd0>, origin='/usr/lib/python3.11/site-packages/Cython/Compiler/FusedNode.cpython-311-x86_64-linux-gnu.so')"

__test__ = {}

