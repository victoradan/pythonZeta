from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.semigroup import Semigroup, mappend

class MaybeSemigroup(Semigroup):
    type = Maybe

    @staticmethod
    def mappend(x, y):
        if x is Nothing: return y
        if y is Nothing: return x
        return Just(x.v |mappend| y.v)
        # is_nothing = y
        # is_just = lambda v: Just (x |mappend| y)
        # return fold(x, is_nothing, is_just)

        # Nothing `mappend` m = m
        # m `mappend` Nothing = m
        # Just m1 `mappend` Just m2 = Just (m1 `mappend` m2)

