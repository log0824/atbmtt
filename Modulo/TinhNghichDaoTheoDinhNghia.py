def modular_inverse_by_definition(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x 
    return None 
a = 7858
n = 6577
x = modular_inverse_by_definition(a, n)
print("Nghịch đảo của", a, "mod", n, "là:", x)
