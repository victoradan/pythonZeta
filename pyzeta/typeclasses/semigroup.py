from .typeclassmeta import TypeClass
from ..infix import Infix

class Semigroup(TypeClass):

    @staticmethod
    def mappend(x, y):
        raise NotImplementedError()

def _mappend(x, y):
    return Semigroup.getClassInstance(type(x)).mappend(x, y)

mappend = Infix(_mappend)

