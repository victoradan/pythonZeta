from .typeclassmeta import TypeClass
from ..infix import Infix


class Applicative(TypeClass):

    @staticmethod
    def app(fab, fa):
        raise NotImplementedError()

    @staticmethod
    def pure(a):
        raise NotImplementedError()

def _app(fab, fa):
    return Applicative.getClassInstance(type(fab)).app(fab, fa)

app = Infix(_app)

