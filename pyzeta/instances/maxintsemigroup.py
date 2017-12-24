from numbers import Number

from pyzeta.typeclasses.semigroup import Semigroup
from pyzeta.registry import register

class MaxSemigroup(Semigroup):

    @staticmethod
    def mappend(x, y):
        return max(x, y)


register('Semigroup', Number, MaxSemigroup)