"""
instance_registry looks like:
{
    'Semigroup': {
                    Number: NumberSemigroup,
                    Maybe: MaybeSemigroup
                },
    'Monoid': {
        Number: NumberMonoid,
        Maybe: MaybeMonoid,
    }
}
"""
from collections import defaultdict
from typing import Dict

INSTANCE_REGISTRY: Dict[str, Dict[type, type]] = defaultdict(dict)

def register(typeclass_name: str, tp: type, instance: type) -> None:
    INSTANCE_REGISTRY[typeclass_name][tp] = instance

def get_instance_cls(typeclass_name: str, type_searched: type) -> type:
    for type_known, instance_cls in INSTANCE_REGISTRY[typeclass_name].items():
        if issubclass(type_searched, type_known):
            return instance_cls
    else:
        raise TypeError("No Instance found for {} {}".format(typeclass_name, 
                                                             type_searched))
