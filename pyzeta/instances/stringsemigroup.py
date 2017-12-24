
from pyzeta.typeclasses.semigroup import Semigroup

class StringSemigroup(Semigroup):
    type = str

    @staticmethod
    def mappend(x, y):
        return x + y

