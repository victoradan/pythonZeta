from pyzeta.instances import *
from pyzeta.datatypes.maybe import Just, Nothing, Maybe
from pyzeta.typeclasses.semigroup import mappend


def test_maybe_semigroup_just_nothing():
    r = Just("abc") |mappend| Nothing
    assert r == Just("abc")

def test_maybe_semigroup_just_just():
    r = Just("abc") |mappend| Just("def")
    assert r == Just("abcdef")

def test_bla():
    from pyzeta.typeclasses.semigroup import Semigroup
    import pprint
    pprint.pprint(Semigroup.registry)