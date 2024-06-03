from pwn import *
from Crypto.Util.number import long_to_bytes

# Establish connection to the remote service
r = remote("titan.picoctf.net", 58378)

# Retrieve the encrypted password from file
with open('password.enc', 'rb') as f:
    c = f.read().decode().strip()

c = int(c)
print(f'c (encrypted password): {c}')

# Create a custom message (m = 2) and convert it to a byte string
m = 2
m_byte = pwnlib.util.packing.p8(m)  # Convert to byte string

# Encrypt the custom message
r.sendlineafter(b'E --> encrypt D --> decrypt.', b'E')
r.sendlineafter(b'enter text to encrypt (encoded length must be less than keysize): ', m_byte)
r.recvuntil(b'ciphertext (m ^ e mod n) ')
ca = int(r.recvline().strip().decode())
print(f'ca (encrypted custom message): {ca}')

# Form the custom ciphertext by multiplying ca and c
cb = ca * c
print(f'cb (custom ciphertext to be decrypted): {cb}')

# Decrypt the custom ciphertext
r.sendlineafter(b'E --> encrypt D --> decrypt.', b'D')
r.sendlineafter(b'Enter text to decrypt: ', str(cb).encode())
r.recvuntil(b'decrypted ciphertext as hex (c ^ d mod n): ')

# Retrieve and decode the decrypted custom ciphertext
cbd = r.recvline().strip().decode()
print(f'cbd (decrypted custom ciphertext in hex): {cbd}')

# Convert cbd from hex to integer
cbd_int = int(cbd, 16)

# Retrieve the real message by dividing by 2 and converting to bytes
t = cbd_int // 2
plaintext = long_to_bytes(t)
print(f'plaintext: {plaintext.decode()}')

# Clean up the connection
r.close()
