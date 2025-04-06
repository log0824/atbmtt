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
def compute_values(a, b, x, y, n):
    ax = tinh(a, x, n)
    by = tinh(b, y, n)

    A1 = (ax + by) % n
    A2 = (ax - by) % n
    A3 = (ax * by) % n

    A4 = e.Extended_euclid(by, n)  
    A5 = None if A4 is None else (ax * A4) % n 

    return A1, A2, A3, A4, A5

a, b, x, y, n = 3, 5, 4, 2, 19
A1, A2, A3, A4, A5 = compute_values(a, b, x, y, n)

print(f"A1 = {A1}")
print(f"A2 = {A2}")
print(f"A3 = {A3}")
print(f"A4 = {A4}")
print(f"A5 = {A5}")