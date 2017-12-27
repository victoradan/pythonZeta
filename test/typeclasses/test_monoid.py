from hypothesis import given
import hypothesis.strategies as st

from pyzeta.typeclasses.semigroup import mappend
from pyzeta.typeclasses.monoid import mempty

## Associativity ##

def test_mempty():
    assert left_identity("abc")
    assert right_identity("abc")

def left_identity(y):
    return (mempty(str) |mappend| y) == y

def right_identity(x):
    return (x |mappend| mempty(str)) == x
