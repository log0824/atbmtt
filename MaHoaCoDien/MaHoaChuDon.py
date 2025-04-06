import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

def maHoaChuDon(m, k):
    d1, key = {}, {}
    cnt = 0
    c = ""
    for i, j in zip(s.ascii_uppercase(), k):
        d1[i] = cnt
        key[cnt] = j
        cnt += 1
    for i in m:
        c += key[d1[s.lowerToUpper(i)]]
    return c

M = "AWOMANGIVESANDFO"
K = "THLEYNPSXADWKFUBOGMQVJRCIZ"
print(maHoaChuDon(M, K))
