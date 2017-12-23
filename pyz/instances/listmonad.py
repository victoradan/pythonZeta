from pyz.typeclasses.monad import Monad

class ListMonad(Monad):
    type = list

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

