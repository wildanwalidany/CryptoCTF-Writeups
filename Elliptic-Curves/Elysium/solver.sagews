from Crypto.Util.number import bytes_to_long, long_to_bytes
from sage.all import *

p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
K = GF(p)
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
E = EllipticCurve(K, (a, b))

G = E.gens()[0]

Q = E(26326686390928441989926437302948364151298187886536227434090842323538336764500, 15057597490574272687879749163595226837809841897797118807290241444796596563842)
print('Q: ', Q)

# Perform scalar multiplication modulo the order of the curve's group
k_inverse = inverse_mod(21, E.order())

# Reverse function
def sub(Q, G):
    return (Q - 288 * G) * k_inverse

# Solve
P = sub(Q, G)
print('P: ', P)
# P:  (30156328313429427284394412836107457667369495430135666824361307261 : 10603528671921342255505831100941791652056909983808240029625305925470899416192 : 1)

print(long_to_bytes(30156328313429427284394412836107457667369495430135666824361307261 ))