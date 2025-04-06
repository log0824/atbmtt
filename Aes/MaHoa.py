import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s

d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def convert_to_state(matrix):
    state = [["" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[i][j] = matrix[2 * (i + j * 4):2 * (i + j * 4) + 2]
    return state

def SUBBYTE(state):
    S_BOX = [
        ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],  
        ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],  
        ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],  
        ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],  
        ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],  
        ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],  
        ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],  
        ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],  
        ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],  
        ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],  
        ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],  
        ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],  
        ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],  
        ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],  
        ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],  
        ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
    ]
    new_state = [["" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            val = state[i][j]
            row_idx = d[val[0]]
            col_idx = d[val[1]] 
            new_state[i][j] = S_BOX[row_idx][col_idx]
    return new_state

def  SHIFTROW(state):
    new_state = [["" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = state[i][(j+i)%4]
    return new_state

def galois_multiply(a, b):
    if isinstance(b, str):
        b = int(b, 16)
    result = 0
    for _ in range(8): 
        if b & 1:
            result ^= a
        carry = a & 0x80
        a = (a << 1) & 0xFF
        if carry:
            a ^= 0x1B
        b >>= 1
    return format(result, '02X')

def MIXCOLUMN(state):
    def mul(a, b):
        return int(galois_multiply(a, b), 16)

    new_state = [["00"] * 4 for _ in range(4)]
    for j in range(4): 
        s0 = int(state[0][j], 16)
        s1 = int(state[1][j], 16)
        s2 = int(state[2][j], 16)
        s3 = int(state[3][j], 16)

        new_state[0][j] = format(mul(2, s0) ^ mul(3, s1) ^ s2 ^ s3, '02X')
        new_state[1][j] = format(s0 ^ mul(2, s1) ^ mul(3, s2) ^ s3, '02X')
        new_state[2][j] = format(s0 ^ s1 ^ mul(2, s2) ^ mul(3, s3), '02X')
        new_state[3][j] = format(mul(3, s0) ^ s1 ^ s2 ^ mul(2, s3), '02X')
    return new_state


def ADDROUNDKEY(state, K):
    K = convert_to_state(K)
    new_state = [["00"] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            s = int(state[i][j], 16)
            k = int(K[i][j], 16)
            new_state[i][j] = format(s ^ k, '02X')
    return new_state