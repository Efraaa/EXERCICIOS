# Programa: Frequência de um número inteiro em vetor de 30 posições
# Feito por: Efraim
# Data de Criação: 07/06

vet30 =[]
for i in range(30):
    n = int(input('Digite um numero'))
    vet30.append(n)

nx = int(input('Digite um valor')) 
aparece = 0  #usado para calcular a frequencia que o numero aparece no vetor
for numero in vet30:
    if nx == numero:
        aparece += 1
print(aparece)