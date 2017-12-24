from pyzeta.datatypes.maybe import Maybe, Just, Nothing, fold
from pyzeta.typeclasses.monad import Monad
from pyzeta.registry import register

class MaybeMonad(Monad):

    @staticmethod
    def bind(ma, f):
        return fold(ma, Nothing, f)

register('Monad', Maybe, MaybeMonad)
