
class TypeClassMeta(type):
    # we use __init__ rather than __new__ here because we want
    # to modify attributes of the class *after* they have been
    # created
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name
            cls.registry[cls] = cls.type
        super(TypeClassMeta, cls).__init__(name, bases, dct)


class TypeClass(metaclass=TypeClassMeta):
    type: object = object()

    @classmethod
    def getClassInstance(cls, t):
        for k, v in cls.registry.items():
            if v == t and (isinstance(k(), cls)):
                return k

    
