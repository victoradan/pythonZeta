from .typeclassmeta import TypeClass
from ..infix import Infix


class Monoid(TypeClass):

    @staticmethod
    def mempty():
        """Identity of `mappend`."""
        raise NotImplementedError()

    @staticmethod
    def mconcat(lst):
        """Fold a list using a Monoid.."""
        raise NotImplementedError()

