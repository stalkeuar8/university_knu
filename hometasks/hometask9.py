
def f(a: int):
    if a < 1:
        return -1

    n = 1
    f = 1
    while f*(n+1) <= a:
        n += 1
        f *= n

    return n


