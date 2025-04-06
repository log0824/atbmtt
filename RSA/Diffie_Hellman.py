import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import Math

def diffie_hellman(q, a, xA, xB):
    yA = Math.tinh(a, xA, q)
    yB = Math.tinh(a, xB, q)
    kA = Math.tinh(yB, xA, q)
    kB = Math.tinh(yA, xB, q)
    return yA, yB, kA, kB

print(diffie_hellman(7523, 5, 387, 247))