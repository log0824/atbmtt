import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def HaBac(a, m, n):
    res = 1
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        m //= 2
    return res
    
def Fermat(a, m, n):
    if Math.ucln(a, n) and Math.is_prime(n):
        m = m%(n-1)
    return HaBac(a, m, n)
print(Fermat(283, 1821, 241))