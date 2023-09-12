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

The challenge provides two files: `main.py` and `result.txt`. The goal is to reverse the encoding performed in `main.py`and retrieve the flag. The encoding function takes a string (data) as input and encodes it using a custom character set and padding scheme. It converts the input string into binary, groups the binary digits into 5-bit chunks, and maps these chunks to characters in the custom character set to produce the encoded result.

To reverse the encoding, we need to remove any padding characters (=) from the end of the encoded string. Map each character in the encoded string back to its corresponding 5-bit binary representation using the custom character set.
Remove any trailing zeros that were added during encoding. And lasty, convert the resulting binary string into bytes.

To overcome the issue of double quotes `(")` inside a string enclosed by double quotes we can use a backslash (\) before the inner double quotes to indicate that they are part of the string and not the string delimiters

`reverse.py`:

```python
def decode(encoded_str):
    charset = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    padd = "="

    # Remove padding characters from the end
    while encoded_str.endswith(padd):
        encoded_str = encoded_str[:-1]

    # Create a binary string by converting characters from the charset back to binary
    binstr = "".join(format(charset.index(char), "05b") for char in encoded_str)

    # Remove any trailing zeros added during encoding
    binstr = binstr.rstrip("0")

    # Convert the binary string to bytes
    decoded_bytes = bytes(int(binstr[i:i+8], 2) for i in range(0, len(binstr), 8))

    return decoded_bytes

# Usage
encoded_str =  "*&(&)<+$*\"$%+?_?:.,[;[+~+{](+`#%,|![{[*;.]^@}@,>'.:@)_\"<+.:?+`>$'\"#$#`=((|};=="
decoded_data = decode(encoded_str)
print(decoded_data.decode())
```

**Flag:** `INTECHFEST{ECC_FUNd4m3nt4l}`
