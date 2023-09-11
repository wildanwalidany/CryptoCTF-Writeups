# Familiar

Platform: Information and Technology Festival 2023

## Description

> Reinventing the wheel can be stupid sometimes.
> >*(Author: aimardcr)*

Two files were attached:

`main.py`:

```python
def encode(data):
    charset = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    padd = "="

    binstr = "".join(format(byte, "08b") for byte in data)
    padding = (5 - len(binstr) % 5) % 5
    binstr += "0" * padding
    groups = [binstr[i:i+5] for i in range(0, len(binstr), 5)]  # groups it into 5-bit chunks

    result = ""
    for group in groups:
        dec = int(group, 2)
        result += charset[dec]

    result += padd * (padding // 2)
    return result

FLAG = "flag{fake_flag_dont_submit}"
print(encode(FLAG.encode()))
```

`result.txt`:

```text
*&(&)<+$*"$%+?_?:.,[;[+~+{](+`#%,|![{[*;.]^@}@,>'.:@)_"<+.:?+`>$'"#$#`=((|};==
```

## Solution

<!-- This code section is a work in progress - TODO: Update with the solucion -->

**Flag:** `INTECHFEST{WhY_W0ulD_AnY0n3_Us3_Th1S_Enc0D1nG?}`
