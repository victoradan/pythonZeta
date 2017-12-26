from pyzeta.typeclasses.monoid import Monoid
from pyzeta.registry import register

class StringMonoid(Monoid):

    @staticmethod
    def mempty():
        return ""

register('Monoid', str, StringMonoid)
