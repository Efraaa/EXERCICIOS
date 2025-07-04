# Programa:Conversão de números romanos (< 4000) para arábicos
# Feito por: Efraim
# Data de Criação: 24/06

romano = input("Digite um número romano: ").upper()

valores = []
for char in romano:
    if char == 'I':
        valores.append(1)
    elif char == 'V':
        valores.append(5)
    elif char == 'X':
        valores.append(10)
    elif char == 'L':
        valores.append(50)
    elif char == 'C':
        valores.append(100)
    elif char == 'D':
        valores.append(500)
    elif char == 'M':
        valores.append(1000)

total = 0
for i in range(len(valores)):
    # Aplica a regra de subtração dos números romanos (ex: IV = 4), subtraindo quando o valor atual é menor que o próximo
    if i < len(valores) - 1 and valores[i] < valores[i + 1]:
        total -= valores[i]
    else:
        total += valores[i]

print(f"Número arábico: {total}")
