"""
RSA encryption algorithm
a method for encrypting a number that uses seperate encryption and decryption keys
this file only implements the key generation algorithm
there are three important numbers in RSA called n, e, and d
e is called the encryption exponent
d is called the decryption exponent
n is called the modulus
these three numbers satisfy
((x ** e) ** d) % n == x % n
to use this system for encryption, n and e are made publicly available, and d is kept secret
a number x can be encrypted by computing (x ** e) % n
the original number can then be recovered by computing (E ** d) % n, where E is
the encrypted number
fortunately, python provides a three argument version of pow() that can compute powers modulo
a number very quickly:
(a ** b) % c == pow(a,b,c)
"""
from algorithms.maths import generate_key


#sample usage:
n,e,d = generate_key(16)
data = 20
encrypted = pow(data,e,n)
decrypted = pow(encrypted,d,n)
assert decrypted == data