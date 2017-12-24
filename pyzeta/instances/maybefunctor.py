
from toolz import compose

from pyzeta.typeclasses.functor import Functor
from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.registry import register

class MaybeFunctor(Functor):

    @staticmethod
    def fmap(f, fa):
        return fold(fa, Nothing, compose(Just, f))

register('Functor', Maybe, MaybeFunctor)