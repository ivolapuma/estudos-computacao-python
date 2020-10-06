from typing import TypeVar, Generic, List, Tuple

T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self, name: str) -> None:
        self._container: List[T] = []
        self._name = name
        self._calls = 0

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def name(self) -> str:
        return self._name

    def increment(self) -> None:
        self._calls += 1

    def calls(self) -> int:
        return self._calls

    def __repr__(self) -> str:
        return "{}={}".format(self._name, repr(self._container))


def setup_towers(n: int) -> Tuple[Stack[int], Stack[int], Stack[int]]:
    a: Stack[int] = Stack("A")
    b: Stack[int] = Stack("B")
    c: Stack[int] = Stack("C")
    for i in range(1, n + 1):
        a.push(i)
    return a, b, c


def print_towers(a: Stack[int], b: Stack[int], c: Stack[int]):
    print("{}  {}  {}".format(a, b, c))


# Funcao recursiva para resolver problema da Torre de Hanoi
# Recebe begin, end e temp que sao objetos do tipo Stack[int] (uma pilha de inteiros), e n que é
# o número de discos a deslocar da Torre A para C, seguindo as regras do problema:
# - disco maior nao pode ficar em cima de disco menor
# - torre C deve ficar igual a torre A no início
#
# número de chamadas recursivas será em razão de n
# f(n) = 2^n + 2^(n-1) - 2
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    begin.increment()
    end.increment()
    temp.increment()
    # print("#calls={}  begin={}  end={}  temp={}  n={}".format(
    # begin.calls(), begin.name(), end.name(), temp.name(), n))
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


if __name__ == "__main__":
    num_discs: int = 23
    tower_a, tower_b, tower_c = setup_towers(num_discs)
    print_towers(tower_a, tower_b, tower_c)
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print_towers(tower_a, tower_b, tower_c)
    print("#calls={}".format(tower_a.calls()))
