from .typeclassmeta import TypeClass

class Semigroup(TypeClass):
    type: object = object()

    @staticmethod
    def append(x, y):
        raise NotImplementedError()

