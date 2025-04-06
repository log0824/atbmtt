class String:
    @staticmethod
    def ascii_lowercase():
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    @staticmethod
    def ascii_uppercase():
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    @staticmethod
    def lowerToUpper(k):
        t = String.ascii_lowercase()
        l = {t[i]: i for i in range(len(t))}
        if k in l:
            return String.ascii_uppercase()[l[k]]
        return k
    @staticmethod
    def slice_string(s, start = 0, end = None):
        tmp = ""
        if end == None:
            end = len(s)
        start = start % len(s) if start < 0 else start
        end = end % len(s) if end < 0 else min(end, len(s)) 
        for i in range(start, end):
            tmp += s[i]
        return tmp
    @staticmethod
    def split_string(s, step = 1):
        return [s[i:i+step] for i in range(0, len(s), step)]
    @staticmethod
    def upper(s):
        tmp = ""
        t = String.ascii_lowercase()
        l = {t[i]: i for i in range(len(t))}
        for i in s:
            if i in t:
                tmp += String.ascii_uppercase()[l[i]]
            else:
                tmp += i
        return tmp
    @staticmethod
    def replace(s, a, b):
        tmp = ""
        for i in s:
            if i == a:
                tmp += b
            else:
                tmp += i
        return tmp

class Math:
    @staticmethod
    def ucln(a, b):
        if b == 0:
            return a
        return Math.ucln(b, a%b)
    
    _primes = []  

    @staticmethod
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        Math._primes = [i for i in range(limit + 1) if is_prime[i]]

    @staticmethod
    def is_prime(n):
        if not Math._primes or Math._primes[-1] < n:
            Math.sieve(max(2*n, 100))  

        return n in Math._primes
    @staticmethod
    def tinh(a, m, n):
        res = 1
        while m > 0:
            if m % 2 == 1:
                res = (res * a) % n
            a = (a * a) % n
            m //= 2
        return res