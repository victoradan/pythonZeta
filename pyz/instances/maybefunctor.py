
from toolz import compose

from pyz.typeclasses.functor import Functor
from pyz.datatypes.maybe import Maybe, Just, Nothing, fold

class MaybeFunctor(Functor):
    type = Maybe

    @staticmethod
    def fmap(f, fa):
        return fold(fa, Nothing, compose(Just, f))
