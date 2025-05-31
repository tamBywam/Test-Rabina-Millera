# Jakub Opólski

import sys
import random

def read_input(filename, fermat_only=False):
    with open(filename, 'r') as f:
        nums = list(map(int, f.read().split()))
    if fermat_only or len(nums) == 1:
        return nums[0], None
    return nums[0], nums[1] if len(nums) == 2 else nums[1] * nums[2] - 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fermat(n, rounds=40):
    if n < 4:
        return n == 2 or n == 3
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        if gcd(a, n) != 1:
            return False, a
        if pow(a, n - 1, n) != 1:
            return False, a
    return True, None

def rabin_miller(n, r=None, rounds=40):
    if n < 4:
        return n == 2 or n == 3, None
    if r is None:
        r = n - 1
    m = r
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        d = gcd(a, n)
        if d > 1:
            return False, d
        b = pow(a, m, n)
        if b == 1 or b == n - 1:
            continue
        for j in range(k):
            b_next = pow(b, 2, n)
            if b_next == 1:
                d1 = gcd(b - 1, n)
                d2 = gcd(b + 1, n)
                if 1 < d1 < n:
                    return False, d1
                if 1 < d2 < n:
                    return False, d2
                return False, None
            if b_next == n - 1:
                break
            b = b_next
        else:
            return False, None
    return True, None

def main():
    fermat_only = '-f' in sys.argv
    n, r = read_input('wejscie.txt', fermat_only)
    test_fn = fermat if fermat_only else rabin_miller
    is_prime, divisor = test_fn(n, r) if not fermat_only else test_fn(n)
    
    if is_prime:
        result = "prawdopodobnie pierwsza"
    elif divisor not in (None, 1, n):
        result = str(divisor)
    else:
        result = "na pewno złożona"

    with open('wyjscie.txt', 'w') as f:
        f.write(result + '\n')

if __name__ == "__main__":
    main()