import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modulo.Euclid_MoRong import Extended_euclid as ex
from My_folder.module import Math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, e):
    n = p*q
    phi = (p-1)*(q-1)
    d = ex(e, phi)
    if d == None:
        return "Không tìm được khóa bí mật d"
    PU = (e, n)
    PR = (d, n)
    return PU, PR

def rsa_encrypt(message, e, n):
    return Math.tinh(message, e, n)

def rsa_decrypt(ciphertext, d, n):
    return Math.tinh(ciphertext, d, n)