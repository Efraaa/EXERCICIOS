# Programa: Cálculo do determinante de uma matriz 3x3 com restrição de código
# Feito por: Efraim
# Data de Criação: 07/06

import random

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 10)) # Preenche matriz com valores aleatórios entre 1 e 10
    matriz.append(linha)

print("Matriz gerada:")
for linha in matriz:
    print(linha)

# Cálculo do determinante pela Regra de Sarrus, dividido em três partes para atender à restrição de no máximo 4 linhas
a = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
b = matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
c = matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
det = a - b + c

print("Determinante da matriz:", det)
