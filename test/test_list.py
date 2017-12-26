from pyzeta.typeclasses.applicative import app
from pyzeta.typeclasses.functor import fmap
from pyzeta.typeclasses.monad import bind
from pyzeta.typeclasses.monoid import mempty


## Monoid ##

def test_mempty_list():
    assert mempty(list) == []

## Functor ##

def test_fmap_list():
    r = (lambda x: x+2) |fmap| [1,2,3]
    assert r == [3,4,5]

## Applicative ##

def test_app_list():
    r = [lambda x: x+2] |app| [1,2,3]
    assert r == [3,4,5]

## Monad ##

def test_bind_list():
    r = [1,2,3] |bind| (lambda x: [x+2]) 
    assert r == [3,4,5]

