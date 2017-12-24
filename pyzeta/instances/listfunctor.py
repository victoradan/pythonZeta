from pyzeta.typeclasses.functor import Functor
from pyzeta.registry import register

class ListFunctor(Functor):

    @staticmethod
    def fmap(f, fa):
        return [f(a) for a in fa]

register('Functor', list, ListFunctor)
