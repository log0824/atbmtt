import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modulo.Euclid_MoRong import Extended_euclid as ex
from My_folder.module import Math

def elgamal_encrypt(q, a, Y_A, M, k):
    C1 = Math.tinh(a, k, q)
    C2 = (M * Math.tinh(Y_A, k, q)) % q
    return C1, C2

def elgamal_decrypt(q, x_A, C1, C2):
    s = Math.tinh(C1, x_A, q)
    s_inv = ex(s, q)
    M = (C2 * s_inv) % q
    return M

def ElGamal(q, a, xA):
    yA = Math.tinh(a, xA, q)
    PU = (q, a, yA)
    print("PU = ", PU)
    print("yA = ", yA)
    print("Mã hóa: ")
    C1, C2 = elgamal_encrypt(q, a, yA, 17, 6)
    print(elgamal_encrypt(q, a, yA, 17, 6))
    print("Giải mã: ")
    print(elgamal_decrypt(q, xA, C1, C2))

ElGamal(19, 10, 5)