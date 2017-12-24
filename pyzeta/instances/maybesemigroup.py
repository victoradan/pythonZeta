from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.semigroup import Semigroup, mappend

from pyzeta.registry import register

class MaybeSemigroup(Semigroup):

    @staticmethod
    def mappend(x, y):
        if x is Nothing: return y
        if y is Nothing: return x
        return Just(x.v |mappend| y.v)
        # is_nothing = y
        # is_just = lambda v: Just (x |mappend| y)
        # return fold(x, is_nothing, is_just)

register('Semigroup', Maybe, MaybeSemigroup)