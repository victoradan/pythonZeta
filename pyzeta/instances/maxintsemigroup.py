from pyzeta.typeclasses.semigroup import Semigroup

class MaxSemigroup(Semigroup):
    type = int

    @staticmethod
    def append(x, y):
        return max(x, y)

