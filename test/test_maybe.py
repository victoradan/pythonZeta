from pyzeta.datatypes.maybe import Just, Nothing, Maybe
from pyzeta.typeclasses.semigroup import mappend
from pyzeta.typeclasses.functor import fmap
from pyzeta.typeclasses.applicative import app
from pyzeta.instances.maybeapplicative import MaybeApplicative


## Semigroup ##

def test_maybe_semigroup_just_nothing():
    r = Just("abc") |mappend| Nothing
    assert r == Just("abc")

def test_maybe_semigroup_just_just():
    r = Just("abc") |mappend| Just("def")
    assert r == Just("abcdef")

## Functor ##

def test_maybe_str_functor_just():
    r = (lambda x: x.upper()) |fmap| Just("abc")
    assert r == Just("ABC")

def test_maybe_str_functor_nothing():
    r = (lambda x: x.upper()) |fmap| Nothing
    assert r == Nothing

def test_maybe_num_functor_just():
    r = (lambda x: x+2) |fmap| Just(3)
    assert r == Just(5)

def test_maybe_num_functor_nothing():
    r = (lambda x: x+2) |fmap| Nothing
    assert r == Nothing

## Applicative ##

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


