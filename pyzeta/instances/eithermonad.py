from pyzeta.datatypes.either import Either, Right
from pyzeta.typeclasses.monad import Monad
from pyzeta.registry import register

class EitherMonad(Monad):

    @staticmethod
    def bind(ma, f):
        if ma.left is not None:
            return ma
        else:
            return f(ma.right)


register('Monad', Either, EitherMonad)
