# Objetivo: Calcular estatísticas das notas de duas turmas.
# Autor: Efraim
# Turma: E2
# Data de Criação: 14/06/2025

import math

print("TURMA 1")
turma1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5, 8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5, 8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]
print(f"Notas originais: {turma1}")
notas = turma1[:]
N = len(notas)

# SELECTION SORT
for i in range(N - 1):
    pos_min = i
    for j in range(i + 1, N):
        if notas[j] < notas[pos_min]:
            pos_min = j
    temp = notas[i]
    notas[i] = notas[pos_min]
    notas[pos_min] = temp

print(f"Notas ordenadas: {notas}")
minimo = notas[0]
maximo = notas[-1]
soma = 0
for i in range(N):
    soma += notas[i]
media = soma / N
soma_quadrados = 0
for i in range(N):
    soma_quadrados += (notas[i] - media) ** 2
desvio_padrao = math.sqrt(soma_quadrados / N)
if N % 2 == 0:
    mediana = (notas[N//2 - 1] + notas[N//2]) / 2
else:
    mediana = notas[N//2]

# BUSCA EXAUSTIVA PARA MODA
moda = notas[0]
maior_freq = 0
for i in range(N):
    frequencia = 0
    for j in range(N):
        if notas[i] == notas[j]:
            frequencia += 1
    if frequencia > maior_freq:
        maior_freq = frequencia
        moda = notas[i]

print(f"Mínimo: {minimo:.1f}")
print(f"Máximo: {maximo:.1f}")
print(f"Média: {media:.1f}")
print(f"Desvio Padrão: {desvio_padrao:.1f}")
print(f"Mediana: {mediana:.1f}")
print(f"Moda: {moda:.1f} ocorre {maior_freq} vezes)")

print("TURMA 2")
turma2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0, 6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]
print(f"Notas originais: {turma2}")
notas = turma2[:]
N = len(notas)

# SELECTION SORT
for i in range(N - 1):
    pos_min = i
    for j in range(i + 1, N):
        if notas[j] < notas[pos_min]:
            pos_min = j
    temp = notas[i]
    notas[i] = notas[pos_min]
    notas[pos_min] = temp

print(f"Notas ordenadas: {notas}")
minimo = notas[0]
maximo = notas[-1]
soma = 0
for i in range(N):
    soma += notas[i]
media = soma / N
soma_quadrados = 0
for i in range(N):
    soma_quadrados += (notas[i] - media) ** 2
desvio_padrao = math.sqrt(soma_quadrados / N)
if N % 2 == 0:
    mediana = (notas[N//2 - 1] + notas[N//2]) / 2
else:
    mediana = notas[N//2]

# BUSCA EXAUSTIVA PARA MODA
moda = notas[0]
maior_freq = 0
for i in range(N):
    frequencia = 0
    for j in range(N):
        if notas[i] == notas[j]:
            frequencia += 1
    if frequencia > maior_freq:
        maior_freq = frequencia
        moda = notas[i]

print(f"Mínimo: {minimo:.1f}")
print(f"Máximo: {maximo:.1f}")
print(f"Média: {media:.1f}")
print(f"Desvio Padrão: {desvio_padrao:.1f}")
print(f"Mediana: {mediana:.1f}")
print(f"Moda: {moda:.1f} ocorre {maior_freq} vezes)")

