from collections import namedtuple


Maybe   = namedtuple('Maybe', ('v',))
# class Maybe(Generic[A]):

    # def __init__(self, value: A) -> None:
        # self.v = value

    # def __eq__(self, other) -> bool:
        # if type(other) is type(self):
            # return self.__dict__ == other.__dict__
        # return False


Just    = lambda x: Maybe(x)
Nothing = Maybe(None)


def fold(maybe, if_nothing, if_just):
    if maybe.v is None:
        return if_nothing
    else:
        return if_just(maybe.v)


