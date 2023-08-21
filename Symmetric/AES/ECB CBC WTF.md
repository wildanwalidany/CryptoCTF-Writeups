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

The provided program performs allows us to encrypt a flag using `AES-CBC` mode and decrypt a ciphertext using `AES-ECB` mode.

Based on the `CBC` and `ECB` algorithm,

![CBC-Encryption](https://upload.wikimedia.org/wikipedia/commons/d/d3/Cbc_encryption.png)
![ECB-Decryption](https://upload.wikimedia.org/wikipedia/commons/6/66/Ecb_decryption.png)

CBC (Cipher Block Chaining) encryption is a block cipher mode that XORs each plaintext block with the previous ciphertext block before encryption, using an initialization vector (IV) for the first block. So the same plaintext blocks dont get encrypted to the ciphertext.

ECB (Electronic Codebook) decryption is a block cipher mode where each ciphertext block is decrypted independently.

From the program, there is interesting line of code:

```python
ciphertext = iv.hex() + encrypted.hex()
```

It can be seen that the ciphertext is concenated with the `IV`. From this information we can extract the `IV` and XOR it to the `ECB` decrypted cipher block to reverse the `CBC` encryption or mimic the `CBC` decryption. From the challenge we know the length of ciphertext is 48 bytes and AES block size is 16 bytes. So the first block is `IV` and the remaining 2 blocks is the actual ciphertext. The scenario to obtain the flag is like this:

```math
flagBlock_{0} = decrypt(cipherBlock_{0}) \oplus IV

flagBlock_{1} = decrypt(cipherBlock_{1}) \oplus cipherBlock_{0}
```
<!-- This code section is a work in progress - TODO: Update with the solucion -->

**flag:** `flag`
