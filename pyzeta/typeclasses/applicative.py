from .typeclassmeta import TypeClass
from ..infix import Infix
from pyzeta.registry import get_instance_cls

class Applicative(TypeClass):

    @staticmethod
    def app(fab, fa):
        raise NotImplementedError()

    @staticmethod
    def pure(a):
        raise NotImplementedError()

## TODO: implement pure (and mempty in Monoid) such that type `t` needs 
## not be given explicitly. 
def pure(t, a):
    return get_instance_cls('Applicative', t).pure(a)

def _app(fab, fa):
    instance_cls = get_instance_cls('Applicative', type(fab))
    return instance_cls.app(fab, fa)

app = Infix(_app)

