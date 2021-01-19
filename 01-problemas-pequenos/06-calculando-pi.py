# O numero pi ou 3.14159... pode ser obtido por varias formulas, dentre elas, a formula de Leibniz,
# que diz que a convergencia da seguinte serie infinita é igual a pi:
#
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == "__main__":
    print("pi com {} termos = {}".format(1, calculate_pi(1)))
    print("pi com {} termos = {}".format(2, calculate_pi(2)))
    print("pi com {} termos = {}".format(5, calculate_pi(5)))
    print("pi com {} termos = {}".format(10, calculate_pi(10)))
    print("pi com {} termos = {}".format(20, calculate_pi(20)))
    print("pi com {} termos = {}".format(50, calculate_pi(50)))
    print("pi com {} termos = {}".format(100, calculate_pi(100)))
    print("pi com {} termos = {}".format(1000, calculate_pi(1000)))
    print("pi com {} termos = {}".format(10000, calculate_pi(10000)))
    print("pi com {} termos = {}".format(100000, calculate_pi(100000)))
    print("pi com {} termos = {}".format(1000000, calculate_pi(1000000)))
