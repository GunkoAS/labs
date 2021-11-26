import math
import sieveoferatothenes as sE
import random



def RSA(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            break
    d = 0
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break
    return [e, n], [d, n]


def encrypt(input, k_public):
    inputencrypt = []
    for m in input:
        inputencrypt.append(pow(ord(m), k_public[0]) % k_public[1])
    return inputencrypt


def decrypt(input, k_private):
    inputdecrypt = ''
    for m in input:
        inputdecrypt += chr(pow(m, k_private[0]) % k_private[1])
    return inputdecrypt


p = sE.get_nth_prime(random.randint(50, 150))
q = sE.get_nth_prime(random.randint(50, 150))

k_public, k_private = RSA(p, q)


print('Публичный ключ:', ", ".join(list(map(str, k_public))))

print('Приватный ключ:', ", ".join(list(map(str, k_private))))

msg = encrypt('Ключ Боба',k_public)
print('Message:', decrypt(msg, k_private))

