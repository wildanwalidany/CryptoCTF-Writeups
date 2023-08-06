PASSWORD = b"give me the flag!!!"
mP = crc32(PASSWORD)
# crc32.py reverse 87619      
# crc32.py reverse 40431
p1,p2 = b'BeSqrm', b'ZJWWgU'

mp1,mp2 = crc32(p1), crc32(p2)

# ensure that the CRC values are indeed factors of the CRC value of the PASSWORD
assert mp1 * mp2 == mP

print(f"Desired CRC: {mP} \n Factors: {mp1} * {mp2}")

s1 = 0
s2 = 0

with remote('signer.chal.imaginaryctf.org',  1337) as P:
    P.recvuntil(b'Get flag')
    P.sendline(b'1')
    P.recvuntil(b'Enter message:')
    P.sendline(p1)
    P.recvuntil(b'Signature: ')
    s1 = int(P.recvline().decode().strip())
    print(f"Received sig1: {s1}")

    P.recvuntil(b'Get flag')
    P.sendline(b'1')
    P.recvuntil(b'Enter message:')
    P.sendline(p2)
    P.recvuntil(b'Signature: ')
    s2 = int(P.recvline().decode().strip())
    print(f"Received sig2: {s2}")

    # Multiply the two signatures together
    s = s1 * s2 

    print(f"Will send: {s}")

    P.recvuntil(b'Get flag')
    P.sendline(b'2')
    P.recvuntil(b'for the password:')
    P.sendline(str(s).encode())
    P.interactive()

    # [*] Switching to interactive mode
    # You win! The flag is ictf{m4ybe_crc32_wasnt_that_secure_after_all_1ab93213}
