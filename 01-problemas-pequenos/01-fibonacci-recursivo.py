from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}  # casos base


# Fibonacci com recursao infinita, nao deve ser chamada!
def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


# Fibonacci com recursao finita (tem caso base), mas para n ~= 50 nao deve funcionar!
def fib2(n: int) -> int:
    if n < 2:  # caso base
        return n
    return fib2(n-1) + fib2(n-2)


# Fibonacci com memoizacao
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)  # memoizacao
    return memo[n]


# Fibonacci com memoizacao de funcao embutida
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # caso base
        return n
    return fib4(n-1) + fib4(n-2)


if __name__ == "__main__":
    # print(fib2(5))
    # print(fib2(10))
    # print(fib2(40))
    print(fib3(5))
    print(fib3(10))
    print(fib3(50))
    print(fib3(80))
    print(fib4(5))
    print(fib4(10))
    print(fib4(50))
