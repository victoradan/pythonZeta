from pyzeta.typeclasses.semigroup import Semigroup
from pyzeta.registry import register
from pyzeta.datatypes.either import Either

class EitherSemigroup(Semigroup):

    @staticmethod
    def mappend(a, b):
        if a.left is not None:
            return b
        else:
            return a

register('Semigroup', Either, EitherSemigroup)
