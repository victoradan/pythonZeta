# PythonZeta

## Overview

PythonZeta is a very modest Python library that implements types and algebras standard to functional programming. It is inspired and influenced by ScalaZ (hence the name). 

This library was written for didactic purposes, as a way to re-enforce and demonstrate learning of FP to myself.

I owe the great majority of the FP I know to Prof. Sukant Hajra, to whom I can't less than dedicate this little piece of work. 
Many thanks also to:

- Jesse Kelly, who implemented a similar library and from whom I took some clever ideas. 
- Sooraj Bhat, from whom I also continue to learn FP. 


## Installation

```bash
pip install pyzeta
```

## Algebras
The following algebras are implemented in the library:

### Semigroup
A Semigroup is a collection of items together with an associative binary operator (here called `|mappend|`). 

### Laws
Associativity:
- `x |mappend| (y |mappend| z) == (x |mappend| y) |mappend| z`

### Monoid
A monoid is is a semigroup having an identity element `mempty`.

#### Laws
Left and right identity:
- `mempty |mappend| y == y`
- `x |mappend| mempty == x`

### Functor
A Functor defines an `|fmap|` interface.

#### Laws
Identity
- `identity |fmap| fa == fa`

Composition
- `g |fmap| (f |fmap| fa) == compose(g, f) |fmap| fa`


### Applicative
Applicative is a Functor that introduces two functions:
- `pure(a)` which wrapps a value `a` in a "context".
- `fg |app| fa` which applies a "wrapped" function `g` in context `f` to the `a` in context `f`. 

#### Laws
Identity

    `f identity |app| fa == fa`

Homomorphism
    `pure(g) |app| pure(a) == pure(g(a))`

Derived map
    `g |fmap| fa == pure(g) |app| fa`

Composition
    ```
    comp_func = lambda bc: lambda ab: compose(bc, ab) 
    lhs = fbc |app| (fab |app| fa)
    rhs = (comp_func |fmap| fbc)  |app| fab |app| fa
    lhs == rhs
    ```
Interchange
  `fg |app| pure(a) == pure(lambda ff: ff(a)) |app| fg`

### Monad
The Monad introduced the `bind` operator the the Applicative:

   `|bind| :: m a -> (a -> m b) -> m b`


