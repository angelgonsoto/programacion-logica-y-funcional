"""Serie de fibonacci"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}", end = "|")


# Versión Optimizada con memorización
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_opt(n):
    if n <= 1:
        return n
    return fibonacci_opt(n - 1) + fibonacci_opt(n - 2)

print(fibonacci_opt(50))