from pyz.datatypes.maybe import *
from pyz.instances import *
from pyz.typeclasses.functor import fmap


def test_fmap():
    r = (lambda x: x+2) |fmap| [1,2,3]
    assert r == [3,4,5]

def test_fmap_maybe():
    r = (lambda x: x+2) |fmap| Just(3)
    assert r == Just(5)

    r = (lambda x: x+2) |fmap| Nothing
    assert r == Nothing


