# Programa: Contagem de números pares em vetor de 40 posições
# Feito por: Efraim
# Data de Criação: 07/06

vet = []
for i in range(40):                      
    n = int(input('Digite o valor'))
    vet.append(n)
    
pares = 0
for valor in vet:  #analisando os valores inseridos no vetor
    if valor % 2 == 0:
        pares += 1

print(pares)