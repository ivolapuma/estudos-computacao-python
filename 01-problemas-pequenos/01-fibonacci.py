
# Fibonacci com recursao infinita, nao deve ser chamada!
def fib1(n : int) -> int:
    return fib1(n-1) + fib1(n-2)

# Fibonacci com recursao finita (tem caso base), mas para n ~= 50 nao deve funcionar!
def fib2(n : int) -> int:
    if n < 2: return n # caso base
    return fib2(n-1) + fib2(n-2)

from typing import Dict

memo: Dict[int, int] = {0:0, 1:1} # casos base

# Fibonacci com memoizacao
def fib3(n : int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) # memoizacao
    return memo[n]

if __name__ == "__main__":
    #print(fib2(5))
    #print(fib2(10))
    #print(fib2(40))
    print(fib3(5))
    print(fib3(10))
    print(fib3(40))
    print(fib3(80))