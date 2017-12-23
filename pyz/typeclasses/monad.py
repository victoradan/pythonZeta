
from .typeclassmeta import TypeClass
from ..infix import Infix


class Monad(TypeClass):

    @staticmethod
    def bind(ma, f):
        raise NotImplementedError()

    # @staticmethod
    # def pure(a):
        # raise NotImplementedError()

def _bind(ma, f):
    return Monad.getClassInstance(type(ma)).bind(ma, f)

bind = Infix(_bind)

