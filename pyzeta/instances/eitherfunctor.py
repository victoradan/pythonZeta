from pyzeta.typeclasses.functor import Functor
from pyzeta.registry import register
from pyzeta.datatypes.either import Either, Right

class EitherFunctor(Functor):

    @staticmethod
    def fmap(f, fa):
        return Right(f(fa.right)) if fa.right else fa

register('Functor', Either, EitherFunctor)
