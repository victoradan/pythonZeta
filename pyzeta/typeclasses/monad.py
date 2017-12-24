
from .typeclassmeta import TypeClass
from ..infix import Infix

from pyzeta.registry import get_instance_cls

class Monad(TypeClass):

    @staticmethod
    def bind(ma, f):
        raise NotImplementedError()

def _bind(ma, f):
    instance_cls = get_instance_cls('Monad', type(ma))
    return instance_cls.bind(ma, f)
    #return Monad.getClassInstance(type(ma)).bind(ma, f)

bind = Infix(_bind)

