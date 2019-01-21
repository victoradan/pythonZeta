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

# (>=>) :: Monad m => (a -> m b) -> (b -> m c) -> (a -> m c)
def _kleisli(f, g):
    return lambda x: f(x) |bind| g


bind = Infix(_bind)

kleisli = Infix(_kleisli)
