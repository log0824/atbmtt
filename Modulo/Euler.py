import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def Euler_phi(n):
    Math.sieve(n)
    d = Math._primes
    tmp = 1
    for i in d:
        if n%i == 0:
            n = n//i
            tmp *= (i-1)
    return tmp