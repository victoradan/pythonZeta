from pyzeta.typeclasses.functor import Functor

class ListFunctor(Functor):
    type = list

    @staticmethod
    def fmap(f, fa):
        return [f(a) for a in fa]

