
from pyz.datatypes.maybe import Maybe, Nothing, Just
from pyz.instances import *
from pyz.typeclasses.applicative import app


def test_app_maybe_just_just():
    r = Just(lambda x: x*2) |app| Just(2) 
    assert r == Just(4)

def test_app_maybe_nothing_just():
    r = Nothing |app| Just(2) 
    assert r == Nothing

def test_app_maybe_just_nothing():
    r = Just(lambda x: x*2) |app| Nothing
    assert r == Nothing


def test_pure():
    r = MaybeApplicative.pure(2)
    assert r == Just(2)
