from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.monoid import Monoid
from pyzeta.registry import register

class MaybeMonoid(Monoid):

    @staticmethod
    def mempty():
        return Nothing

register('Monoid', Maybe, MaybeMonoid)