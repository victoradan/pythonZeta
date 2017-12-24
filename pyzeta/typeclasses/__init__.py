from .applicative import Applicative, app
from .functor import Functor, fmap
from .monad import Monad, bind
from .semigroup import Semigroup

"""

int |mappend| int

type Semigroup type


registry = {Number: NumberSemigroup}
registry = {
                Semigroup: {
                                Number: NumberSemigroup,
                                Maybe: MaybeSemigroup
                            },
                Monoid: {
                    Number: NumberMonoid,
                    Maybe: MaybeMonoid,
                }
            }

for type, instance in registry[Semigroup]:
    if isinstance(val, type): return instance
"""