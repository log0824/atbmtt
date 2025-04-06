a, m, n = 31, 315, 391
def tinh(a, m, n):
    if m == 1:
        return a%n
    if m % 2 == 0:
        m = m//2
        a = (a**m % n)**2 % n
    else:
        m = (m-1)//2
        a = ((a**m % n)**2)*a % n
    tinh(a, m, n)
    return a
print(tinh(a, m, n))