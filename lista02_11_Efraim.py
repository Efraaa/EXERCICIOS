# Programa: Ordenação de vetor com 100 elementos sem usar sort()
# Feito por: Efraim
# Data de Criação: 07/06

import random
vet = []
for _ in range(100):
    vet.append(random.randint(1,10))

vet_ordenado = vet[:]

tam = len(vet_ordenado)
for i in range(tam-1): # Ordenação do vetor usando o método de seleção (Selection Sort), comparando e trocando o menor valor restante
    pmin = i
    for j in range(i+1,tam):
        if vet_ordenado[j]< vet_ordenado[pmin]:
            pmin = j
        temp = vet_ordenado[i]
        vet_ordenado[i]=vet_ordenado[pmin]
        vet_ordenado[pmin]= temp
print(vet)
print(vet_ordenado)