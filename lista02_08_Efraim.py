# Programa: Simulação de caixa eletrônico com quantidade limitada de notas
# Feito por: Efraim
# Data de Criação: 07/06

valores = [100, 50, 20, 10, 5, 1]
quantidades = [10, 10, 10, 10, 10, 10]

while True:
    valor = int(input("Digite o valor a sacar (0 para sair): "))
    if valor == 0:
        print("Operação encerrada.")
        break
    valor_original = valor
    notas_usadas = [0, 0, 0, 0, 0, 0]
    quant_temp = quantidades[:]  #Cópia temporária para testar o saque sem afetar o estoque original
    for i in range(len(valores)):
        qtd_necessaria = valor // valores[i]
        qtd_disponivel = quant_temp[i] # Cria uma cópia temporária das quantidades de notas para simular o saque sem alterar as originais até a confirmação

        if qtd_necessaria <= qtd_disponivel:
            qtd_usada = qtd_necessaria
        else:
            qtd_usada = qtd_disponivel

        notas_usadas[i] = qtd_usada
        valor -= qtd_usada * valores[i]
        quant_temp[i] -= qtd_usada

    if valor == 0:
        quantidades = quant_temp
        print(f"Saque de R$ {valor_original} autorizado.")
        for i in range(len(valores)):
            if notas_usadas[i] > 0:
                print(f"Notas de {valores[i]}: quantidade de notas usadas {notas_usadas[i]}")
    else:
        print("Não é possível realizar o saque com as notas disponíveis.")