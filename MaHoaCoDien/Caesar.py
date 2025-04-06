import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

def Caesar(m, k):
    d1, d2 = {}, {}
    cnt = 0
    c = ""
    for i in s.ascii_uppercase():
        d1[i] = cnt
        d2[cnt] = i
        cnt += 1
    for i in m:
        if s.lowerToUpper(i) in d1: 
            c += d2[(d1[i] + k) % 26]
        else:
            c += i
    return c

M = "NOROSEWITHOUTATH"
K = 8
print(Caesar(M, K))
