import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math
import Euler

def tinh(a, m, n):
    res = 1
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        m //= 2
    return res

def tinh_Luy_Thua(a, m, n):
    p = Euler.Euler_phi(n)
    if Math.ucln(a, n) == 1:
        return tinh(a, m%p, n)
    if m < (p + 1):
        return tinh(a, m, n)
    return (a*tinh(a, m-(p+1), n))%n    