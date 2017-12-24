from pyzeta.typeclasses.semigroup import Semigroup
from pyzeta.registry import register

class ListSemigroup(Semigroup):

    @staticmethod
    def mappend(x, y):
        return x + y

register('Semigroup', list, ListSemigroup)
