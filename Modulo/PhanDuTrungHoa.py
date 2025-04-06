import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math
import Euclid_MoRong as e
import Euler_luyThua as Eu


def phanDuTrungHoa(a, k, n):
    Math.sieve(n)
    d = Math._primes
    s = []
    tmp = n
    for i in d:
        if n%i == 0:
            n = n//i
            s.append(i)
    A = 0
    for i in s:
        ai = Eu.tinh_Luy_Thua(a, k, i)
        Mi = tmp//i
        ci = Mi*e.Extended_euclid(Mi, i)
        A += ai*ci
    return A%tmp
