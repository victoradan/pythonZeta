
from .typeclassmeta import TypeClass
from ..infix import Infix
from pyzeta.registry import get_instance_cls

class Semigroup(TypeClass):

    @staticmethod
    def mappend(x, y):
        raise NotImplementedError()

def _mappend(x, y):
    instance_cls = get_instance_cls('Semigroup', type(x))
    return instance_cls.mappend(x, y)

mappend = Infix(_mappend)

