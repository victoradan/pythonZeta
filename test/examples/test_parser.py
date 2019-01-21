import toolz

from pyzeta.datatypes.maybe import Just, Nothing, Maybe
from pyzeta.infix import Infix
from pyzeta.instances.maybemonad import MaybeMonad
from pyzeta.typeclasses.monad import kleisli

const = toolz.curry(lambda a, b: a)
fail = const(Nothing)
pasz = Just

#and_then = toolz.curry(lambda v1, v2: v1 |kleisli| v2)
and_then = Infix(lambda v1, v2: v1 |kleisli| v2)

# valid_char :: Char -> Validator
def valid_char(c):
    # Validator :: str -> Maybe str
    def validator(s: str):
        return Just(s[1:]) if len(s) > 0 and s[0] == c else Nothing
    return validator

wrapped = toolz.curry(lambda l, r, v: valid_char(l) |and_then| v |and_then| valid_char(r))

wrapped_round = wrapped('(')(')')

def test_example():
    r = wrapped_round(pasz)('()after')
    assert r == Just('after')
