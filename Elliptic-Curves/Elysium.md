# Elysium

Platform: Information and Technology Festival 2023

## Description

> The paradise of ~~underworld~~ (cryptography)
> >*(Author: merricx)*

Two files were attached:

`challenge.sage`:

```python
from Crypto.Util.number import bytes_to_long
from sage.all import *


def add(G, P):
    return G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + P + P + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + \
        G + G + P + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + P + G + G + P + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + G + \
        G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + G + \
        G + G + G + G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + G + \
        G + G + G + G + G + P + G + G + G + G + G + G + G + G + G + G + P + G + G


flag = open('flag.txt', 'rb').read()

p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
K = GF(p)
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
E = EllipticCurve(K, (a, b))

G = E.gens()[0]

m = bytes_to_long(flag)
P = E.lift_x(Integer(m))
Q = add(G, P)

print('Q:', Q)
```

`output.txt`:

```text
Q: (26326686390928441989926437302948364151298187886536227434090842323538336764500 : 15057597490574272687879749163595226837809841897797118807290241444796596563842 : 1)
```

## Solution

<!-- This code section is a work in progress - TODO: Update with the solucion -->

**Flag:** `INTECHFEST{ECC_FUNd4m3nt4l}`
