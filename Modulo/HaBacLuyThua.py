
def tinh(a, m, n):
    res = 1
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        m //= 2
    return res