def tao_bang_hoan_vi(m, key):
    so_cot = len(key)
    hang = (len(m) + so_cot - 1) // so_cot 
    bang = [['X'] * so_cot for _ in range(hang)] 

    index = 0
    for i in range(hang):
        for j in range(so_cot):
            if index < len(m):
                bang[i][j] = m[index]
                index += 1
    return bang

def ma_hoa(m, key):
    key_thu_tu = sorted(range(len(key)), key=lambda k: key[k])  
    bang = tao_bang_hoan_vi(m, key)
    cipher_text = ""
    for i in key_thu_tu:
        for hang in bang:
            cipher_text += hang[i]
    return cipher_text

M = "ABADBEGINNINGMAKES"
KEY = [2, 3, 1, 5, 4]
print(ma_hoa(M, KEY))
