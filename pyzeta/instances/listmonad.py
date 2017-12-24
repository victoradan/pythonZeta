from pyzeta.typeclasses.monad import Monad
from pyzeta.registry import register

class ListMonad(Monad):

    @staticmethod
    def bind(ma, f):
        result = []
        mmb = [f(a) for a in ma]
        for mb in mmb:
            result.extend(mb)
        return result

    @staticmethod
    def pure(a):
        return [a]

register('Monad', list, ListMonad)
