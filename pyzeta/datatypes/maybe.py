from collections import namedtuple


Maybe   = namedtuple('Maybe', ('v',))

Just    = lambda x: Maybe(x)
Nothing = Maybe(None)


def fold(maybe, if_nothing, if_just):
    if maybe.v is None:
        return if_nothing
    else:
        return if_just(maybe.v)

