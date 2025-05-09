# Code for A383738
# Author Darío Clavijo, 2025.

def queens(n, row=0, cols=0, pos_diags=0, neg_diags=0, sol=None, mask=None):
    if sol is None:
        sol = []
        mask = (1 << n) - 1
    if row == n:
        yield sol[:]
    else:
        free = ~(cols | pos_diags | neg_diags) & mask
        while free:
            lsb = free & -free
            col = lsb.bit_length() - 1
            sol.append(col)
            yield from queens(n, row + 1,
                              cols | lsb,
                              (pos_diags | lsb) << 1,
                              (neg_diags | lsb) >> 1,
                              sol,
                              mask)
            sol.pop()
            free ^= lsb
is_square_perm = lambda p, sqrt: p == [sqrt[sqrt[i]] for i in range(len(sqrt))]
def a(n):
    c = 0
    for sol in queens(n):
        if not is_square_perm(list(range(n))[::-1], sol): c += 1
    return c
print([a(n) for n in range(1, 14)])
