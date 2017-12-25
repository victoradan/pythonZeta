from pyzeta.typeclasses.applicative import Applicative
from pyzeta.typeclasses.functor import fmap
from pyzeta.registry import register

class ListApplicative(Applicative):

    @staticmethod
    def app(fab, fa):
        return [f(x) for x in fa for f in fab]

    @staticmethod
    def pure(a):
        return [a]

register('Applicative', list, ListApplicative)
