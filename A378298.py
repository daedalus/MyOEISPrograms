# Code for A378298
# Author Darío Clavijo, 2024.

from sympy.core.intfunc import isqrt
from collections import defaultdict

def a(n: int) -> int:
    if n < 4: return [0, 0, 0, 1][n]
    i2, s = isqrt(n), defaultdict(int)
    P = [x*x for x in range(0, i2-1)]
    P += [pow(x, 2, n) for x in range(i2-1, (n >> 1)+1)]
    P += P[::-1][not (n & 1):]
    for i in range(1, len(P)): s[P[i]] += 1
    K = {x: x*(x-1) >> 1 for x in set(s.values())}
    return sum(K[v] for v in s.values())

print([a(n) for n in range(1, 69)])
