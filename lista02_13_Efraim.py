# Programa:Conversão de números arábicos (< 4000) para romanos
# Feito por: Efraim
# Data de Criação: 24/06

numero = int(input("Digite um número (1 a 3999): "))

if numero < 1 or numero >= 4000:
    print("Número fora do intervalo!")
else:

    milhares = ["", "M", "MM", "MMM"]
    centenas  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    dezenas   = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades  = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    m = numero // 1000
    c = (numero % 1000) // 100
    d = (numero % 100) // 10
    u = numero % 10
# Concatena os símbolos romanos de cada casa decimal para formar o número completo
    numero_romano = milhares[m] + centenas[c] + dezenas[d] + unidades[u]

    print("Número romano:", numero_romano)
