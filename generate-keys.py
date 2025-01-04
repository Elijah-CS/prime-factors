import util

modulusSize = 1024

msg = "Hello, World!"

primeSize = modulusSize // 2
p = util.getRandomPrime(primeSize)
q = util.getRandomPrime(primeSize)
while p == q:
    q = util.getRandomPrime(primeSize)

n, e, d = util.getKeys(p, q)

encodedMsg = util.encodeMessage(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)
decodedMsg = util.decodeMessage(decryptedMsg)

print("p: ", p)
print("q: ", q)
print("Public key (e, n):")
print("\te = ", e)
print("\tn = ", n)
print("\nPrivate key (d, n):")
print("\td = ", d)
print("\tn = ", n)
print("\nOriginal message string:\n\t", msg)
print("\nInteger encoded message:\n\t", encodedMsg)
print("\nEncrypted message( C(M) = M^e % n ):\n\t", encryptedMsg)
print("\nDecrypted message( M(C) = C^d % n ):\n\t", decryptedMsg)
print("\nDecoded Original message string:\n\t", decodedMsg)


data = {
    "public": {
        "e": e,
        "n": n
    },
    "private": {
        "p": p,
        "q": q,
        "d": d,
        "n": n
    },
    "original_message": msg,
    "encoded_message": encodedMsg,
    "encrypted_message": encryptedMsg
}

import yaml

with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)