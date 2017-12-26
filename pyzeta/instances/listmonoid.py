from pyzeta.typeclasses.monoid import Monoid
from pyzeta.registry import register

class ListMonoid(Monoid):

    @staticmethod
    def mempty():
        return []

register('Monoid', list, ListMonoid)
