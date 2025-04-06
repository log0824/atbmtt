import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from My_folder.module import String as s
import MaHoa
import SinhKhoa

m = "18DC9095F9149EDB7323F20E4E462D92"
k = "CFD61D489E7C48BC46C9F875C1F04E1B"

def AES(m, k):
    state = MaHoa.convert_to_state(m)
    state = MaHoa.ADDROUNDKEY(state, k)
    state = MaHoa.SUBBYTE(state)
    state = MaHoa.SHIFTROW(state)
    state = MaHoa.MIXCOLUMN(state)
    Key = SinhKhoa.KeyExpansion(k)
    for i in range(0, 8):
        state = MaHoa.ADDROUNDKEY(state, Key[i])
        state = MaHoa.SUBBYTE(state)
        state = MaHoa.SHIFTROW(state)
        state = MaHoa.MIXCOLUMN(state)
    state = MaHoa.ADDROUNDKEY(state, Key[8])
    state = MaHoa.SUBBYTE(state)
    state = MaHoa.SHIFTROW(state)
    state = MaHoa.ADDROUNDKEY(state, Key[9])
    C = ""
    for i in range(4):
        for j in range(4):
            C += state[j][i]
    print(C)
AES(m, k)