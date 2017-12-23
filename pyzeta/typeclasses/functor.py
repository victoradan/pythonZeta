from .typeclassmeta import TypeClass
from ..infix import Infix

class Functor(TypeClass):
    type: object = object()

    @staticmethod
    def fmap(f, fa):
        raise NotImplementedError()


def _fmap(f, fa):
    return Functor.getClassInstance(type(fa)).fmap(f, fa)

fmap = Infix(_fmap)
