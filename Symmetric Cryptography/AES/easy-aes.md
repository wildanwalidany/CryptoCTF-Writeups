
# easy-aes
Platform: Gemastik 2023

## Description
> Attack on AES OFB

Author: prajnapras19

```
nc ctf-gemastik.ub.ac.id 10002
```

`chall.py`:
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

key = os.urandom(AES.key_size[0])
iv = os.urandom(AES.block_size)
secret = bytes_to_long(os.urandom(128))

def encrypt(pt):
    bytes_pt = long_to_bytes(pt)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    padded_pt = pad(bytes_pt, AES.block_size)
    return bytes_to_long(cipher.encrypt(padded_pt))

def menu():
    print('===== Menu =====')
    print('1. Encrypt')
    print('2. Get encrypted secret')
    print('3. Get flag')
    print('4. Exit')
    choice = int(input('> '))
    return choice

def get_flag():
    res = int(input('secret: '))
    if secret == res:
        os.system('cat flag.txt')
        print()

while True:
    try:
        choice = menu()
        if choice == 1:
            pt = int(input('plaintext = '))
            ciphertext = encrypt(pt)
            print(f'{ciphertext = }')
        if choice == 2:
            ciphertext = encrypt(secret)
            print(f'{ciphertext = }')
        if choice == 3:
            get_flag()
            break
        if choice == 4:
            break
    except:
        print('something error happened.')
        break

print('bye.')
```
## Solution
From what we see here, the gen.py program opens text.txt file that contains the flag, converts it to hexadecimal, and replaces each hexadecimal digit with a randomly shuffled emoji. The encoded text is then saved in `out.txt`. With this information, we can attempt to reverse the process using `frequency analysis`.

`script`:
```python
from pwn import *
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote("ctf-gemastik.ub.ac.id", 10002) # (host, port)

# create custom 128-bytes plaintext
t = os.urandom(128)
p1 = str(bytes_to_long(t))

# custom ciphertext
r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'plaintext = ', p1.encode())
r.recvuntil(b"ciphertext = ")
c1 = int(r.recvline().strip())

# get the secret_ciphertext
r.sendlineafter(b'> ', b'2')
r.recvuntil(b"ciphertext = ")
c2 = int(r.recvline().strip())

# get the secret
p2 = str(bytes_to_long(unpad(long_to_bytes(bytes_to_long(pad(t, AES.block_size)) ^ c1 ^ c2), AES.block_size)))

# get the flag
r.sendlineafter(b'> ', b'3')
r.sendlineafter(b'secret: ', p2.encode())
r.interactive()
```

**flag:** `gemastik{crypto_easy-aes_66ed4a79865d667a1981763e84019607d3f2c0a69e7cb97f}`
