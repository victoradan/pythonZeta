from toolz import identity, compose

from hypothesis import given
import hypothesis.strategies as st

from pyzeta.typeclasses.applicative import app, pure
from pyzeta.typeclasses.functor import fmap
from pyzeta.datatypes.maybe import Maybe

## TODO: use hypothesis

def test_applicative_identity():
    assert_applicative_identity([identity], [1,2])

def test_applicative_homomorphism():
    assert_applicative_homomorphism(list, lambda x: x+1, 1)
    assert_applicative_homomorphism(Maybe, lambda x: x+1, 1)

def test_applicative_derived_map():
    assert_applicative_derived_map(list, [1], lambda x: x+1)

def test_applicative_composition():
    assert_applicative_composition([lambda x: x*2], [lambda x: x-2], [1])

def test_applicative_interchange():
    assert_applicative_interchange([lambda x: x+1], 1)


## Laws ##

def assert_applicative_identity(fi, fa):
    assert fi |app| fa == fa

def assert_applicative_homomorphism(t, ab, a):
    assert pure(t, ab) |app| pure(t, a) == pure(t, ab(a))

def assert_applicative_derived_map(t, fa, f):
    assert f |fmap| fa == pure(t, f) |app| fa

def assert_applicative_composition(fab, fbc, fa):
    comp_func = lambda bc: lambda ab: compose(bc, ab) 
    lhs = fbc |app| (fab |app| fa)
    rhs = (comp_func |fmap| fbc)  |app| fab |app| fa
    assert lhs == rhs

def assert_applicative_interchange(fab, a):
    assert fab |app| pure(list, a) == pure(list, lambda ff: ff(a)) |app| fab
