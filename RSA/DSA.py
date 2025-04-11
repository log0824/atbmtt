import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modulo.Euclid_MoRong import Extended_euclid as ex
from My_folder.module import Math

def dsa(p, q, h, xA, k, H_M):
    g = Math.tinh(h, (p-1)//q, p)
    yA = Math.tinh(g, xA, p)
    r = Math.tinh(g, k, p)%q
    s = (ex(k, q)*((H_M + xA*r)%q))%q
    w = ex(s, q)
    u1 = (H_M*w)%q
    u2 = (r*w)%q
    v = (((Math.tinh(g, u1, p))*(Math.tinh(yA, u2, p)))%p)%q
    print(f"Khóa công khai yA = {yA}")
    print(f"Chữ kí số (r, s): ({r}, {s})")
    if v == r:
        return True
    else:
        return False
print(dsa(47, 23, 7, 13, 5, 11))
