from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.monoid import Monoid

class MaybeMonoid(Monoid):
    type = Maybe

    @staticmethod
    def mempty():
        return Nothing
