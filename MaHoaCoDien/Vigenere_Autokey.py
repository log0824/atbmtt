import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

def vigenere_LapKhoa(m, k):
    d1, d2 = {}, {}
    cnt = 0
    c = ""
    key = k + s.slice_string(m, 0, len(m) - len(k))
    for i in s.ascii_uppercase():
        d1[i] = cnt
        d2[cnt] = i
        cnt += 1
    for i, j in zip(m, key):
        c += d2[(d1[s.lowerToUpper(i)] + d1[s.lowerToUpper(j)])%26]
    return c

m = "MONEYMAKESTHE"
k = "YOUREON"
print(vigenere_LapKhoa(m, k))
    