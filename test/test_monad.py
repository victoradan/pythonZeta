from pyz.instances import *
from pyz.typeclasses.monad import bind


def test_bind_list():
    r = [1,2,3] |bind| (lambda x: [x+2]) 
    assert r == [3,4,5]

