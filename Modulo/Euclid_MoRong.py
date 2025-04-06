import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def Extended_euclid(a, n):
    a1, a2 = 0, n
    b1, b2 = 1, a
    if a>n:
        a = a%n
    while b2!=1:
        q = a2//b2
        t1, t2 = a1 - q*b1, a2-q*b2
        a1, a2 = b1, b2
        b1, b2 = t1, t2
        if b2 == 0:
            print("Không tìm được nghịch đảo")
            return None
    return b1%n
def modular_exponentiation(a, b, n):
    if b < 0:
        a = Extended_euclid(a, n) 
        if a is None:
            return "Không thể tính toán"
        b = -b  
    res = 1
    while b:
        if b % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        b //= 2
    return res