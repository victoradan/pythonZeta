
from pyz.datatypes.maybe import Maybe, Just, Nothing, fold
from pyz.typeclasses.monad import Monad

class MaybeMonad(Monad):
    type = Maybe

    @staticmethod
    def bind(ma, f):
        return fold(ma, Nothing, f)

    # @staticmethod
    # def pure(a):
        # return  Maybe(a)
