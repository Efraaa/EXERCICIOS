# Programa: Impressão dos N primeiros números primos
# Feito por: Efraim
# Data de Criação: 07/06

n = int(input("Digite quantos números primos deseja ver: "))
contador_primos = 0
numero_atual = 2  

while contador_primos < n:
    divisores = 0
    for i in range(2, numero_atual):
        if numero_atual % i == 0: 
            divisores += 1 # Conta os divisores para saber se é primo
    if divisores == 0: # Verifica se o número atual não tem divisores além de 1 e ele mesmo (ou seja, é primo)
        print(numero_atual)
        contador_primos += 1
    numero_atual += 1

