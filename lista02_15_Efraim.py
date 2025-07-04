# Programa:Decomposição de número em fatores primos (ex: '3^33', '7^4', ...)
# Feito por: Efraim
# Data de Criação: 24/06

num = int(input("Digite um número inteiro para fatorar: "))
fatores = []
divisor = 2
# Testa divisores até a raiz quadrada de num para fatoração em primos (mais eficiente que testar até num)
while divisor * divisor <= num:
    contador = 0
    while num % divisor == 0:
        num //= divisor
        contador += 1
    if contador > 0:
        fatores.append(f"{divisor}^{contador}")
    if divisor == 2:
        divisor = 3
    else:
        divisor += 2

if num > 1:
    fatores.append(f"{num}^1")

print(fatores)
