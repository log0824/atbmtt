import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math
import Euclid_MoRong as e
import Euler_luyThua as Eu
import Euler

def tinh(a, m, n):
    res = 1
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        m //= 2
    return res

def canNguyenThuy(a, n):
    if Math.ucln(a, n) != 1:
        print(f"{a} không là căn nguyên thủy của {n}")
        return
    p = Euler.Euler_phi(n)
    d = []
    for i in range(2, int(p**0.5) + 1):
        if p%i == 0:
            d.append(i)
            d.append(p//i)
    d.append(p)
    t = 0
    for i in d:
        if tinh(a, i, n) == 1:
            t = i
            break
    if t == p:
        print(f"{a} là căn nguyên thủy của {n}")
        return
    else:
        print(f"{a} không là căn nguyên thủy của {n}")
        return