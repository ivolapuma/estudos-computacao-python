import sys


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # começa com uma sentinela
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # desloca dois bits para a esquerda
            if nucleotide == "A":  # muda os dois ultimos bits para 00
                self.bit_string |= 0b00
            elif nucleotide == "C":  # muda os dois ultimos bits para 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # muda os dois ultimos bits para 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # muda os dois ultimos bits para 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11  # obtem apenas 2 bits relevantes
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] inverte a string usando fatiamento com inversao

    def __str__(self) -> str:  # representacao em string para exibicao elegante
        return self.decompress()


# exemplo de uso de sys.getsizeof()
def exemplo_getsizeof() -> None:
    print(sys.getsizeof(1))
    print(sys.getsizeof(10))
    print(sys.getsizeof(1000))
    print(sys.getsizeof(1000000))


def teste_CompressedGene() -> None:
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(sys.getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compacta
    print("compressed is {} bytes".format(sys.getsizeof(compressed.bit_string)))
    print(compressed)  # descompacta
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))


def teste_CompressedGene2() -> None:
    s = "ACGTAACCGGTT"
    print("string {} tem {} bytes".format(s, sys.getsizeof(s)))
    cg = CompressedGene(s)
    print("seq bits {} tem {} bytes".format(cg.bit_string, sys.getsizeof(cg.bit_string)))
    s2 = cg.decompress()
    print("string descomprimida {}".format(s2))
    print("string {} e string descomprimida {} sao iguais: {}".format(s, s2, s == s2))


if __name__ == "__main__":
    # exemplo_getsizeof()
    # teste_CompressedGene()
    teste_CompressedGene2()