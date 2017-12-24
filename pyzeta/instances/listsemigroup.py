from pyzeta.typeclasses.semigroup import Semigroup

class ListSemigroup(Semigroup):
    type = list

    @staticmethod
    def mappend(x, y):
        return x + y

