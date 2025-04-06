import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math
import Euclid_MoRong as e
import Euler_luyThua as Eu
import Euler

def tinh(a, b, n):
    a %= n
    b %= n
    if b == 1:
        return 0
    m = int(n**0.5) + 1
    tmp = 1
    d = {}
    for j in range(m):
        d[tmp] = j
        tmp = (tmp*a)%n
    nd = e.modular_exponentiation(a, (-1)*m, n)
    tmp = b
    for i in range(m):
        if tmp in d:
            return i * m + d[tmp]
        tmp = (tmp*nd)%n
    return None

a, b, n = 3, 5, 19
k = tinh(a, b, n)
if k is not None:
    print(f"Logarithm rời rạc của {b} theo cơ số {a} modulo {n} là: {k}")
else:
    print(f"Không tìm thấy giá trị k thỏa mãn {a}^k ≡ {b} (mod {n})")
