from .typeclassmeta import TypeClass
from ..infix import Infix

from pyzeta.registry import get_instance_cls

class Monoid(TypeClass):

    @staticmethod
    def mempty():
        """Identity of `mappend`."""
        raise NotImplementedError()

    @staticmethod
    def mconcat(lst):
        """Fold a list using a Monoid.."""
        raise NotImplementedError()

def mempty(t):
    instance_cls = get_instance_cls('Monoid', t)
    return instance_cls.mempty()


