from hypothesis import given
import hypothesis.strategies as st

from pyzeta.typeclasses.semigroup import mappend

## Associativity ##

@given(st.text(), st.text(), st.text())
def test_associativity(x, y, z):
    assert associativity(x, y, z)

def associativity(x, y, z):
    return ((x |mappend| y) |mappend| z) == (x |mappend| (y |mappend| z))
