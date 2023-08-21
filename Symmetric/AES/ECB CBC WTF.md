# ECB CBC WTF

Platform: Cryptohack

## Description

> Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?

`play at:` [ecbcbcwtf](https://aes.cryptohack.org/ecbcbcwtf)

`source:`

```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```

## Solution

<!-- This code section is a work in progress - TODO: Update with the solucion -->

**flag:** `flag`
