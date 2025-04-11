import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def Euler_phi(n):
    Math.sieve(n)
    d = Math._primes
    phi = n
    for p in d:
        if p*p > n:
            break
        if n%p == 0:
            while n%p == 0:
                n //= p
            phi -= phi//p
    if n > 1:
        phi -= phi//n
    return phi