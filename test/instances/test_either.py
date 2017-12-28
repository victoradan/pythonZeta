from pyzeta.typeclasses.applicative import app
from pyzeta.typeclasses.functor import fmap
from pyzeta.typeclasses.monad import bind
from pyzeta.typeclasses.monoid import mempty
from pyzeta.typeclasses.semigroup import mappend
from pyzeta.datatypes.either import Right, Left


## Semogroup ##

def test_mappend_either():
    assert Right(1)  |mappend| Right(2)  == Right(1)
    assert Right(1)  |mappend| Left("e") == Right(1)
    assert Left("e") |mappend| Right(2)  == Right(2)
    assert Left("e") |mappend| Left("e") == Left("e")


## Functor ##

def test_fmap_either():
    f = lambda x: x+1
    assert f |fmap| Right(1)  == Right(2)
    assert f |fmap| Left("e") == Left("e")

## Applicative ##

def test_app_either():
    f = lambda x: x+1
    assert Right(f) |app| Right(1)   == Right(2)
    assert Right(f) |app| Left("e")  == Left("e")
    assert Left("e") |app| Right(1)  == Left("e")
    assert Left("e") |app| Left("x") == Left("e")
    

## Monad ##

def test_bind_either():
    f = lambda x: Right(x+1)
    assert Right(1)  |bind| f == Right(2)
    assert Left("e") |bind| f == Left("e")

