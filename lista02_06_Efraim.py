# Programa: Cálculo do valor de π por série
# Feito por: Efraim
# Data de Criação: 07/06

import math
n = int(input())

par = 0
impar = 0
for i in range(n):
    if i % 2 == 0: 
        par += (1/((i+1)**2))     # Soma os termos de índice par da série
    else:
        impar += (1/((i+1)**2))  # Soma os termos de índice ímpar da série

# Soma alternada das frações 1/(i+1)^2 com sinais diferentes para pares e ímpares,
# usada para aproximar π com a fórmula: π ≈ sqrt(12 * (soma de termos alternados))
res = math.sqrt(12*(par-impar))

print(res)