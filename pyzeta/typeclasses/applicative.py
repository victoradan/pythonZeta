from .typeclassmeta import TypeClass
from ..infix import Infix
from pyzeta.registry import get_instance_cls

class Applicative(TypeClass):

    @staticmethod
    def app(fab, fa):
        raise NotImplementedError()

    @staticmethod
    def pure(a):
        raise NotImplementedError()

def _app(fab, fa):
    instance_cls = get_instance_cls('Applicative', type(fab))
    return instance_cls.app(fab, fa)
    #return Applicative.getClassInstance(type(fab)).app(fab, fa)

app = Infix(_app)

