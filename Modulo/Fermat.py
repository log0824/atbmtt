import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def HaBac(a, m, n):
    if m == 1:
        return a % n
    if m % 2 == 0:
        half = HaBac(a, m // 2, n)
        return (half * half) % n
    else:
        half = HaBac(a, (m - 1) // 2, n)
        return (half * half * a) % n
    
def Fermat(a, m, n):
    if Math.ucln(a, n) and Math.is_prime(n):
        m = m%(n-1)
    return HaBac(a, m, n)
print(Fermat(283, 1821, 241))