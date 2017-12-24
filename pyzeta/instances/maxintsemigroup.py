from pyzeta.typeclasses.semigroup import Semigroup

class MaxSemigroup(Semigroup):
    type = int

    @staticmethod
    def mappend(x, y):
        return max(x, y)

