
def f(n: int):
    if n < 0:
        raise ValueError("n must be 0 or bigger")

    a_k = 1
    print(f"C({n}, {n}) = {a_k}")

    for k in range(n):
        a_k *= n + k + 1
        a_k //= k + 1
        print(f"C({n+k+1}, {n}) = {a_k}")
