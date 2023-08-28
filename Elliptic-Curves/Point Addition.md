# Point Addition

Platform: Cryptohack

## Description

> We will work with the following elliptic curve, and prime: $E: Y^{2}=X^{3}+497X+1768, p:9739$
> Using the above curve, and the point $P(493, 5564)$, $Q(1539,4742)$, $R(4403,5202)$ find the point $S(x,y) = P + P + Q + R$.
> After calculating S, substitute the coordinates into the curve. Assert that the point $S$ is in $E(F_{p})$

## Solution

The Algorithm for the addition of two points in ECC follows these rules:
![ECC_addition](https://github.com/wildanwalidany/CryptoCTF-Writeups/assets/74038077/afc555fa-1b4a-45c3-8aed-ea06210bf4f4)

So we just need to implement the algorithm.

`addition.py`:
```python
<!-- This code section is a work in progress - TODO: Update with the solucion -->
```

**flag:** `flag`
