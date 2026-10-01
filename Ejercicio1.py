import math

N = 10

donas_lista = [(math.sqrt(2)) ** (n - 1) for n in range(1, N + 1)]

donas_dict = {n: (math.sqrt(2)) ** (n - 1) for n in range(1, N + 1)}