# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _accelerated_sequence_clustering
else:
    import _accelerated_sequence_clustering

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _accelerated_sequence_clustering.delete_SwigPyIterator

    def value(self):
        return _accelerated_sequence_clustering.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _accelerated_sequence_clustering.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _accelerated_sequence_clustering.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _accelerated_sequence_clustering.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _accelerated_sequence_clustering.SwigPyIterator_equal(self, x)

    def copy(self):
        return _accelerated_sequence_clustering.SwigPyIterator_copy(self)

    def next(self):
        return _accelerated_sequence_clustering.SwigPyIterator_next(self)

    def __next__(self):
        return _accelerated_sequence_clustering.SwigPyIterator___next__(self)

    def previous(self):
        return _accelerated_sequence_clustering.SwigPyIterator_previous(self)

    def advance(self, n):
        return _accelerated_sequence_clustering.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _accelerated_sequence_clustering.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _accelerated_sequence_clustering.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _accelerated_sequence_clustering.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _accelerated_sequence_clustering.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _accelerated_sequence_clustering.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _accelerated_sequence_clustering.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.SwigPyIterator_swigregister(SwigPyIterator)
class VecDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _accelerated_sequence_clustering.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _accelerated_sequence_clustering.VecDouble___nonzero__(self)

    def __bool__(self):
        return _accelerated_sequence_clustering.VecDouble___bool__(self)

    def __len__(self):
        return _accelerated_sequence_clustering.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _accelerated_sequence_clustering.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _accelerated_sequence_clustering.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _accelerated_sequence_clustering.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _accelerated_sequence_clustering.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _accelerated_sequence_clustering.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _accelerated_sequence_clustering.VecDouble___setitem__(self, *args)

    def pop(self):
        return _accelerated_sequence_clustering.VecDouble_pop(self)

    def append(self, x):
        return _accelerated_sequence_clustering.VecDouble_append(self, x)

    def empty(self):
        return _accelerated_sequence_clustering.VecDouble_empty(self)

    def size(self):
        return _accelerated_sequence_clustering.VecDouble_size(self)

    def swap(self, v):
        return _accelerated_sequence_clustering.VecDouble_swap(self, v)

    def begin(self):
        return _accelerated_sequence_clustering.VecDouble_begin(self)

    def end(self):
        return _accelerated_sequence_clustering.VecDouble_end(self)

    def rbegin(self):
        return _accelerated_sequence_clustering.VecDouble_rbegin(self)

    def rend(self):
        return _accelerated_sequence_clustering.VecDouble_rend(self)

    def clear(self):
        return _accelerated_sequence_clustering.VecDouble_clear(self)

    def get_allocator(self):
        return _accelerated_sequence_clustering.VecDouble_get_allocator(self)

    def pop_back(self):
        return _accelerated_sequence_clustering.VecDouble_pop_back(self)

    def erase(self, *args):
        return _accelerated_sequence_clustering.VecDouble_erase(self, *args)

    def __init__(self, *args):
        _accelerated_sequence_clustering.VecDouble_swiginit(self, _accelerated_sequence_clustering.new_VecDouble(*args))

    def push_back(self, x):
        return _accelerated_sequence_clustering.VecDouble_push_back(self, x)

    def front(self):
        return _accelerated_sequence_clustering.VecDouble_front(self)

    def back(self):
        return _accelerated_sequence_clustering.VecDouble_back(self)

    def assign(self, n, x):
        return _accelerated_sequence_clustering.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _accelerated_sequence_clustering.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _accelerated_sequence_clustering.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _accelerated_sequence_clustering.VecDouble_reserve(self, n)

    def capacity(self):
        return _accelerated_sequence_clustering.VecDouble_capacity(self)
    __swig_destroy__ = _accelerated_sequence_clustering.delete_VecDouble

# Register VecDouble in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.VecDouble_swigregister(VecDouble)
class VecInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _accelerated_sequence_clustering.VecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _accelerated_sequence_clustering.VecInt___nonzero__(self)

    def __bool__(self):
        return _accelerated_sequence_clustering.VecInt___bool__(self)

    def __len__(self):
        return _accelerated_sequence_clustering.VecInt___len__(self)

    def __getslice__(self, i, j):
        return _accelerated_sequence_clustering.VecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _accelerated_sequence_clustering.VecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _accelerated_sequence_clustering.VecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _accelerated_sequence_clustering.VecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _accelerated_sequence_clustering.VecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _accelerated_sequence_clustering.VecInt___setitem__(self, *args)

    def pop(self):
        return _accelerated_sequence_clustering.VecInt_pop(self)

    def append(self, x):
        return _accelerated_sequence_clustering.VecInt_append(self, x)

    def empty(self):
        return _accelerated_sequence_clustering.VecInt_empty(self)

    def size(self):
        return _accelerated_sequence_clustering.VecInt_size(self)

    def swap(self, v):
        return _accelerated_sequence_clustering.VecInt_swap(self, v)

    def begin(self):
        return _accelerated_sequence_clustering.VecInt_begin(self)

    def end(self):
        return _accelerated_sequence_clustering.VecInt_end(self)

    def rbegin(self):
        return _accelerated_sequence_clustering.VecInt_rbegin(self)

    def rend(self):
        return _accelerated_sequence_clustering.VecInt_rend(self)

    def clear(self):
        return _accelerated_sequence_clustering.VecInt_clear(self)

    def get_allocator(self):
        return _accelerated_sequence_clustering.VecInt_get_allocator(self)

    def pop_back(self):
        return _accelerated_sequence_clustering.VecInt_pop_back(self)

    def erase(self, *args):
        return _accelerated_sequence_clustering.VecInt_erase(self, *args)

    def __init__(self, *args):
        _accelerated_sequence_clustering.VecInt_swiginit(self, _accelerated_sequence_clustering.new_VecInt(*args))

    def push_back(self, x):
        return _accelerated_sequence_clustering.VecInt_push_back(self, x)

    def front(self):
        return _accelerated_sequence_clustering.VecInt_front(self)

    def back(self):
        return _accelerated_sequence_clustering.VecInt_back(self)

    def assign(self, n, x):
        return _accelerated_sequence_clustering.VecInt_assign(self, n, x)

    def resize(self, *args):
        return _accelerated_sequence_clustering.VecInt_resize(self, *args)

    def insert(self, *args):
        return _accelerated_sequence_clustering.VecInt_insert(self, *args)

    def reserve(self, n):
        return _accelerated_sequence_clustering.VecInt_reserve(self, n)

    def capacity(self):
        return _accelerated_sequence_clustering.VecInt_capacity(self)
    __swig_destroy__ = _accelerated_sequence_clustering.delete_VecInt

# Register VecInt in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.VecInt_swigregister(VecInt)
class VecUInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _accelerated_sequence_clustering.VecUInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _accelerated_sequence_clustering.VecUInt___nonzero__(self)

    def __bool__(self):
        return _accelerated_sequence_clustering.VecUInt___bool__(self)

    def __len__(self):
        return _accelerated_sequence_clustering.VecUInt___len__(self)

    def __getslice__(self, i, j):
        return _accelerated_sequence_clustering.VecUInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _accelerated_sequence_clustering.VecUInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _accelerated_sequence_clustering.VecUInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _accelerated_sequence_clustering.VecUInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _accelerated_sequence_clustering.VecUInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _accelerated_sequence_clustering.VecUInt___setitem__(self, *args)

    def pop(self):
        return _accelerated_sequence_clustering.VecUInt_pop(self)

    def append(self, x):
        return _accelerated_sequence_clustering.VecUInt_append(self, x)

    def empty(self):
        return _accelerated_sequence_clustering.VecUInt_empty(self)

    def size(self):
        return _accelerated_sequence_clustering.VecUInt_size(self)

    def swap(self, v):
        return _accelerated_sequence_clustering.VecUInt_swap(self, v)

    def begin(self):
        return _accelerated_sequence_clustering.VecUInt_begin(self)

    def end(self):
        return _accelerated_sequence_clustering.VecUInt_end(self)

    def rbegin(self):
        return _accelerated_sequence_clustering.VecUInt_rbegin(self)

    def rend(self):
        return _accelerated_sequence_clustering.VecUInt_rend(self)

    def clear(self):
        return _accelerated_sequence_clustering.VecUInt_clear(self)

    def get_allocator(self):
        return _accelerated_sequence_clustering.VecUInt_get_allocator(self)

    def pop_back(self):
        return _accelerated_sequence_clustering.VecUInt_pop_back(self)

    def erase(self, *args):
        return _accelerated_sequence_clustering.VecUInt_erase(self, *args)

    def __init__(self, *args):
        _accelerated_sequence_clustering.VecUInt_swiginit(self, _accelerated_sequence_clustering.new_VecUInt(*args))

    def push_back(self, x):
        return _accelerated_sequence_clustering.VecUInt_push_back(self, x)

    def front(self):
        return _accelerated_sequence_clustering.VecUInt_front(self)

    def back(self):
        return _accelerated_sequence_clustering.VecUInt_back(self)

    def assign(self, n, x):
        return _accelerated_sequence_clustering.VecUInt_assign(self, n, x)

    def resize(self, *args):
        return _accelerated_sequence_clustering.VecUInt_resize(self, *args)

    def insert(self, *args):
        return _accelerated_sequence_clustering.VecUInt_insert(self, *args)

    def reserve(self, n):
        return _accelerated_sequence_clustering.VecUInt_reserve(self, n)

    def capacity(self):
        return _accelerated_sequence_clustering.VecUInt_capacity(self)
    __swig_destroy__ = _accelerated_sequence_clustering.delete_VecUInt

# Register VecUInt in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.VecUInt_swigregister(VecUInt)
class VecVecDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _accelerated_sequence_clustering.VecVecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _accelerated_sequence_clustering.VecVecDouble___nonzero__(self)

    def __bool__(self):
        return _accelerated_sequence_clustering.VecVecDouble___bool__(self)

    def __len__(self):
        return _accelerated_sequence_clustering.VecVecDouble___len__(self)

    def __getslice__(self, i, j):
        return _accelerated_sequence_clustering.VecVecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _accelerated_sequence_clustering.VecVecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble___setitem__(self, *args)

    def pop(self):
        return _accelerated_sequence_clustering.VecVecDouble_pop(self)

    def append(self, x):
        return _accelerated_sequence_clustering.VecVecDouble_append(self, x)

    def empty(self):
        return _accelerated_sequence_clustering.VecVecDouble_empty(self)

    def size(self):
        return _accelerated_sequence_clustering.VecVecDouble_size(self)

    def swap(self, v):
        return _accelerated_sequence_clustering.VecVecDouble_swap(self, v)

    def begin(self):
        return _accelerated_sequence_clustering.VecVecDouble_begin(self)

    def end(self):
        return _accelerated_sequence_clustering.VecVecDouble_end(self)

    def rbegin(self):
        return _accelerated_sequence_clustering.VecVecDouble_rbegin(self)

    def rend(self):
        return _accelerated_sequence_clustering.VecVecDouble_rend(self)

    def clear(self):
        return _accelerated_sequence_clustering.VecVecDouble_clear(self)

    def get_allocator(self):
        return _accelerated_sequence_clustering.VecVecDouble_get_allocator(self)

    def pop_back(self):
        return _accelerated_sequence_clustering.VecVecDouble_pop_back(self)

    def erase(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble_erase(self, *args)

    def __init__(self, *args):
        _accelerated_sequence_clustering.VecVecDouble_swiginit(self, _accelerated_sequence_clustering.new_VecVecDouble(*args))

    def push_back(self, x):
        return _accelerated_sequence_clustering.VecVecDouble_push_back(self, x)

    def front(self):
        return _accelerated_sequence_clustering.VecVecDouble_front(self)

    def back(self):
        return _accelerated_sequence_clustering.VecVecDouble_back(self)

    def assign(self, n, x):
        return _accelerated_sequence_clustering.VecVecDouble_assign(self, n, x)

    def resize(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble_resize(self, *args)

    def insert(self, *args):
        return _accelerated_sequence_clustering.VecVecDouble_insert(self, *args)

    def reserve(self, n):
        return _accelerated_sequence_clustering.VecVecDouble_reserve(self, n)

    def capacity(self):
        return _accelerated_sequence_clustering.VecVecDouble_capacity(self)
    __swig_destroy__ = _accelerated_sequence_clustering.delete_VecVecDouble

# Register VecVecDouble in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.VecVecDouble_swigregister(VecVecDouble)
class VecVecInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _accelerated_sequence_clustering.VecVecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _accelerated_sequence_clustering.VecVecInt___nonzero__(self)

    def __bool__(self):
        return _accelerated_sequence_clustering.VecVecInt___bool__(self)

    def __len__(self):
        return _accelerated_sequence_clustering.VecVecInt___len__(self)

    def __getslice__(self, i, j):
        return _accelerated_sequence_clustering.VecVecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _accelerated_sequence_clustering.VecVecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _accelerated_sequence_clustering.VecVecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _accelerated_sequence_clustering.VecVecInt___setitem__(self, *args)

    def pop(self):
        return _accelerated_sequence_clustering.VecVecInt_pop(self)

    def append(self, x):
        return _accelerated_sequence_clustering.VecVecInt_append(self, x)

    def empty(self):
        return _accelerated_sequence_clustering.VecVecInt_empty(self)

    def size(self):
        return _accelerated_sequence_clustering.VecVecInt_size(self)

    def swap(self, v):
        return _accelerated_sequence_clustering.VecVecInt_swap(self, v)

    def begin(self):
        return _accelerated_sequence_clustering.VecVecInt_begin(self)

    def end(self):
        return _accelerated_sequence_clustering.VecVecInt_end(self)

    def rbegin(self):
        return _accelerated_sequence_clustering.VecVecInt_rbegin(self)

    def rend(self):
        return _accelerated_sequence_clustering.VecVecInt_rend(self)

    def clear(self):
        return _accelerated_sequence_clustering.VecVecInt_clear(self)

    def get_allocator(self):
        return _accelerated_sequence_clustering.VecVecInt_get_allocator(self)

    def pop_back(self):
        return _accelerated_sequence_clustering.VecVecInt_pop_back(self)

    def erase(self, *args):
        return _accelerated_sequence_clustering.VecVecInt_erase(self, *args)

    def __init__(self, *args):
        _accelerated_sequence_clustering.VecVecInt_swiginit(self, _accelerated_sequence_clustering.new_VecVecInt(*args))

    def push_back(self, x):
        return _accelerated_sequence_clustering.VecVecInt_push_back(self, x)

    def front(self):
        return _accelerated_sequence_clustering.VecVecInt_front(self)

    def back(self):
        return _accelerated_sequence_clustering.VecVecInt_back(self)

    def assign(self, n, x):
        return _accelerated_sequence_clustering.VecVecInt_assign(self, n, x)

    def resize(self, *args):
        return _accelerated_sequence_clustering.VecVecInt_resize(self, *args)

    def insert(self, *args):
        return _accelerated_sequence_clustering.VecVecInt_insert(self, *args)

    def reserve(self, n):
        return _accelerated_sequence_clustering.VecVecInt_reserve(self, n)

    def capacity(self):
        return _accelerated_sequence_clustering.VecVecInt_capacity(self)
    __swig_destroy__ = _accelerated_sequence_clustering.delete_VecVecInt

# Register VecVecInt in _accelerated_sequence_clustering:
_accelerated_sequence_clustering.VecVecInt_swigregister(VecVecInt)

def accelerated_sequence_clustering_approximated(*args):
    return _accelerated_sequence_clustering.accelerated_sequence_clustering_approximated(*args)

def accelerated_sequence_clustering_approximated2(*args):
    return _accelerated_sequence_clustering.accelerated_sequence_clustering_approximated2(*args)

def accelerated_sequence_clustering_approximated3(*args):
    return _accelerated_sequence_clustering.accelerated_sequence_clustering_approximated3(*args)

def accelerated_sequence_clustering(*args):
    return _accelerated_sequence_clustering.accelerated_sequence_clustering(*args)

def basic_sequence_clustering(*args):
    return _accelerated_sequence_clustering.basic_sequence_clustering(*args)

def basic_sequence_clustering_2d(*args):
    return _accelerated_sequence_clustering.basic_sequence_clustering_2d(*args)

def accelerated_sequence_clustering_approximated3_2d(nrows, k, MAX_STALL, theta):
    return _accelerated_sequence_clustering.accelerated_sequence_clustering_approximated3_2d(nrows, k, MAX_STALL, theta)

