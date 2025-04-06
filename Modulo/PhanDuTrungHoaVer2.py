import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math
import Euclid_MoRong as e
import Euler_luyThua as Eu


def phanDuTrungHoa(m, a):
    M = 1
    A = 0
    for i in m:
        M *= i
    for i, j in zip(m, a):
        Mi = M//i
        ci = Mi*e.Extended_euclid(Mi, i)
        A += j*ci
    return A%M

m = [17, 19, 11]
a = [5, 16, 3]
print(phanDuTrungHoa(m, a))