from pyzeta.instances.eitherfunctor import EitherFunctor
from pyzeta.registry import register
from pyzeta.datatypes.either import Either, Right

class EitherApplicative(EitherFunctor):

    @classmethod
    def app(cls, fab, fa):
        if fab.left is not None:
            return fab
        else:
            return cls.fmap(fab.right, fa)

    @staticmethod
    def pure(a):
        return Right(a)

register('Applicative', Either, EitherApplicative)
