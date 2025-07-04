# Programa: Troca das 8 primeiras com as 8 últimas posições em vetor de 16 elementos
# Feito por: Efraim
# Data de Criação: 07/06

vetinvertido = [] #vetor para exibir a ordem esperada(invertida)
vetor_2meta = [] # vetor com os valore da segunda metade
vetor_1meta = [] # vetor com os valores da primeira metade
vetor = []

for i in range(16):
    n = int(input('Digite o os valores do vetor'))
    vetor.append(n)
    
metade = (len(vetor)/2)
for i in range(int(metade)):    #usando a metade
    vetor_1meta.append(vetor[i])

for valor in vetor:
    if valor not in vetor_1meta: 
        vetor_2meta.append(valor)

for valor in vetor_2meta:
    vetinvertido.append(valor)
for valor in vetor_1meta:
    vetinvertido.append(valor)

print(vetor)   
print(vetinvertido)
    