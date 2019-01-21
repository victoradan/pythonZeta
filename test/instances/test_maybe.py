from hypothesis import given
import hypothesis.strategies as st

from pyzeta.datatypes.maybe import Just, Nothing, Maybe
from pyzeta.typeclasses.semigroup import mappend
from pyzeta.typeclasses.functor import fmap
from pyzeta.typeclasses.applicative import app
from pyzeta.instances.maybeapplicative import MaybeApplicative
from pyzeta.typeclasses.monad import bind, kleisli


## Semigroup ##

@given(st.text())
def test_maybe_semigroup_just_nothing(s):
    r = Just(s) |mappend| Nothing
    assert r == Just(s)

@given(st.text())
def test_maybe_semigroup_nothing_just(s):
    r = Nothing |mappend| Just(s)
    assert r == Just(s)

@given(st.text(), st.text())
def test_maybe_semigroup_just_just(s1, s2):
    r = Just(s1) |mappend| Just(s2)
    assert r == Just(s1 + s2)

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

## Monad ##

def test_maybe_monad_bind():
    f = lambda x: Just(x + 1)
    r = Just(1) |bind| f
    assert r == Just(2)

## TODO: Hypothesis
def test_maybe_monad_kleisli():
    f = lambda x: Just(x + 1)
    g = lambda x: Just(x + 2)
    k = f |kleisli| g
    assert k(1) == Just(4)

    f = lambda x: Nothing
    g = lambda x: Just(x + 2)
    k = f |kleisli| g
    assert k(1) == Nothing

    f = lambda x: Just(x + 1)
    g = lambda x: Nothing
    k = f |kleisli| g
    assert k(1) == Nothing

