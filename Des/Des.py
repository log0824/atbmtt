import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s
import MaHoa
import SinhKhoa

d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
h = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

k = "B35F59255E3BCB54"
m = "32D604E6C4504149"

def HexToBin(k):
    return ''.join(MaHoa.hexToBin(d[i]) for i in k)

def chuyenDoi(k):
    tmp = 0
    for i in range(len(k)):
        tmp += int(k[len(k) - i - 1])*(2**i)
    return tmp

def BinToHex(k):
    d = s.split_string(k, 4)
    tmp = ""
    for i in d:
        tmp += h[chuyenDoi(i)]
    return tmp

def DichVong(C0, D0):
    Key = []
    C, D = [], []
    C.append(C0)
    D.append(D0)
    S = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(1, len(S)):
        C.append(SinhKhoa.ShiftLeft(C[i-1], S[i]))
        D.append(SinhKhoa.ShiftLeft(D[i-1], S[i]))
        Ki = SinhKhoa.PC2(C[i], D[i])
        Key.append(Ki)
    return Key

def DES(k, m):
    k = HexToBin(k)
    K1 = SinhKhoa.PC1(k)
    C0, D0 = SinhKhoa.SPLIT_KEY(K1)
    Key = DichVong(C0, D0)
    M = MaHoa.IP(HexToBin(m))
    L0, R0 = MaHoa.SPLIT(M)
    R, L = [], []
    R.append(R0)
    L.append(L0)
    for i in range(0, len(Key)):
        L.append(R[i])
        ERi = MaHoa.E(R[i])
        A = MaHoa.XOR(ERi, Key[i])
        B = MaHoa.SUB(A)
        F = MaHoa.P(B)
        R.append(MaHoa.XOR(L[i], F))
    LR = R[16] + L[16]
    IP_1 = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    C = ''.join(LR[pos - 1] for pos in IP_1)
    print(BinToHex(C))
DES(k, m)