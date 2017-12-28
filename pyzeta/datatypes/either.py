from collections import namedtuple


Either   = namedtuple('Either', ('left','right'))


Right = lambda r: Either(None, r)
Left  = lambda l: Either(l, None)

