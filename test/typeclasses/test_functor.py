from toolz import identity, compose, curry

from hypothesis import given
import hypothesis.strategies as st

from pyzeta.typeclasses.functor import fmap

## TODO: use hypothesis

def test_functor_identity():
    assert_functor_identity([1,2,3])

def test_functor_composition():
    f = lambda x: x+1
    g = lambda x: x+2
    fa = [1,2,3]
    assert_functor_composition(f, g, fa)

def test_functor_curried():
    f = curry(fmap)
    assert f(lambda x: x+1)([1,2,3]) == [2,3,4]

def test_functor_as_func():
    assert fmap(lambda x: x+1, [1,2,3]) == [2,3,4]

## Laws ##

def assert_functor_identity(fa):
    assert identity |fmap| fa == fa

def assert_functor_composition(f, g, fa):
    assert g |fmap| (f |fmap| fa) == compose(g, f) |fmap| fa 




