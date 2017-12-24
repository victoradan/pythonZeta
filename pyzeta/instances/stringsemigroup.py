from pyzeta.typeclasses.semigroup import Semigroup
from pyzeta.registry import register

class StringSemigroup(Semigroup):

    @staticmethod
    def mappend(x, y):
        return x + y


register('Semigroup', str, StringSemigroup)