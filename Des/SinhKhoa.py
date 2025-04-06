import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

def PC1(K):
    if len(K) != 64 or not all(bit in '01' for bit in K):
        raise ValueError("Chuỗi đầu vào phải là chuỗi nhị phân 64 bit.")
    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    K1 = ''.join(K[pos - 1] for pos in PC1)
    return K1

def SPLIT_KEY(K1, C = None, D = None):
    if len(K1) != 56 or not all(bit in '01' for bit in K1):
        raise ValueError("Chuỗi đầu vào phải là chuỗi nhị phân 56 bit.")
    d = s.split_string(K1, len(K1)//2)
    C, D = d[0], d[1]
    return C, D

def ShiftLeft(x, s_1):
    if len(x) != 28 or not all(bit in '01' for bit in x):
        raise ValueError("Chuỗi đầu vào phải là chuỗi nhị phân 28 bit.")
    s_1 %= 28
    return s.slice_string(x, s_1, len(x)) + s.slice_string(x, 0, s_1)

def PC2(C, D):
    if len(C) != 28 or not all(bit in '01' for bit in C):
        raise ValueError("Chuỗi đầu vào phải là chuỗi nhị phân 28 bit.")
    if len(D) != 28 or not all(bit in '01' for bit in D):
        raise ValueError("Chuỗi đầu vào phải là chuỗi nhị phân 28 bit.")
    tmp = C+D
    PC2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    Ks = ''.join(tmp[pos-1] for pos in PC2)
    return Ks