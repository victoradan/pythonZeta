
from pyz.datatypes.maybe import Maybe, Just, Nothing, fold
from pyz.typeclasses.applicative import Applicative
from pyz.typeclasses.functor import fmap
from pyz.instances.maybefunctor import MaybeFunctor

class MaybeApplicative(Applicative):
    type = Maybe

    @staticmethod
    def app(fab, ma):
        #fa = lambda f: MaybeFunctor.fmap(f, ma)
        fa = lambda f:  f |fmap| ma
        return fold(fab, Nothing, fa)

    @staticmethod
    def pure(a):
        return  Maybe(a)

