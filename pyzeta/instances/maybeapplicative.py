
from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.applicative import Applicative
from pyzeta.typeclasses.functor import fmap
from pyzeta.instances.maybefunctor import MaybeFunctor

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

