from hypothesis import given
import hypothesis.strategies as st

from pyzeta.typeclasses.semigroup import mappend
from pyzeta.typeclasses.monoid import mempty

## Associativity ##

def test_mempty():
    assert_left_identity("abc")
    assert_right_identity("abc")

def assert_left_identity(y):
    assert (mempty(str) |mappend| y) == y

def assert_right_identity(x):
    assert (x |mappend| mempty(str)) == x
