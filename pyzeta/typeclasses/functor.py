from .typeclassmeta import TypeClass
from ..infix import Infix
from pyzeta.registry import get_instance_cls

class Functor(TypeClass):
    type: object = object()

    @staticmethod
    def fmap(f, fa):
        raise NotImplementedError()


def _fmap(f, fa):
    instance_cls = get_instance_cls('Functor', type(fa))
    return instance_cls.fmap(f, fa)
    #return Functor.getClassInstance(type(fa)).fmap(f, fa)

fmap = Infix(_fmap)
