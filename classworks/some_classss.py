def factorial_d(n: int) -> int:
    if not isinstance(n, (int, float)):
        raise TypeError("тільки цілі числа")
    
    if isinstance(n, float):
        n = int(n)
    
    if n < 0:
        raise ValueError("тільки невід'ємні числа")
        
    if n in (0, 1):
        return 1
    
    result = 1
    for i in range(n, 1, -2):
        result *= i
        
    return result

for n in range(0, 10):
    print(factorial_d(n))

