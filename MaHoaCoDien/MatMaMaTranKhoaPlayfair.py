import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

M = "THETRUTHWILLOU"
K = "THEDIEIS"

def chiaCapBanRo(m):
    d = []
    i = 0 
    m = s.upper(m)
    m = s.replace(m, "J", "I")
    while i < len(m):
        if i + 1 < len(m): 
            if m[i] == m[i + 1]:
                d.append(m[i] + "X")
                i += 1  
            else:
                d.append(m[i] + m[i + 1])
                i += 2  
        else:  
            d.append(m[i] + "X")
            i += 1  
    return d

def maTranKhoaPlayfair(k):
    d = set()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    k = s.upper(k)
    k = s.replace(k, "J", "I")
    key_string = ""
    for char in k:
        if char not in d and char in alphabet:
            key_string += char
            d.add(char)
    for char in alphabet:
        if char not in d:
            key_string += char
            d.add(char)
    return [list(key_string[i:i+5]) for i in range(0, 25, 5)]

def timViTri(ma_tran, ky_tu):
    for i in range(5):
        for j in range(5):
            if ma_tran[i][j] == ky_tu:
                return i, j
    return None

def maHoaPlayfair(m, k):
    maTran = maTranKhoaPlayfair(k)
    cacCapBanRo = chiaCapBanRo(m)
    ban_ma = ""
    for cap in cacCapBanRo:
        hang1, cot1 = timViTri(maTran, cap[0])
        hang2, cot2 = timViTri(maTran, cap[1])

        if hang1 == hang2:  
            ban_ma += maTran[hang1][(cot1 + 1) % 5]
            ban_ma += maTran[hang2][(cot2 + 1) % 5]
        elif cot1 == cot2:
            ban_ma += maTran[(hang1 + 1) % 5][cot1]
            ban_ma += maTran[(hang2 + 1) % 5][cot2]
        else: 
            ban_ma += maTran[hang1][cot2]
            ban_ma += maTran[hang2][cot1]

    return ban_ma

print(maHoaPlayfair(M, K))