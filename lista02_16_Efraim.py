# Programa:Geração de todas as subsequências não contínuas de uma sequência
# Feito por: Efraim
# Data de Criação: 25/06

sequencia = [1, 2, 3, 4]
subsequencias_nao_continuas = []

tamanho = len(sequencia)
# Gera todas as subsequências possíveis usando máscaras binárias, excluindo a vazia
for i in range(1, 2**tamanho):
   subsequencia_atual = []
   
   for j in range(tamanho):
       if i & (1 << j):
           subsequencia_atual.append(sequencia[j])
   
   if len(subsequencia_atual) >= 2:
       eh_continua = True
       
       posicoes = []
       for elemento in subsequencia_atual:
           posicoes.append(sequencia.index(elemento))
       
       for k in range(len(posicoes) - 1):
           if posicoes[k+1] - posicoes[k] != 1:
               eh_continua = False
               break
       
       if not eh_continua:
           subsequencias_nao_continuas.append(subsequencia_atual)

print(subsequencias_nao_continuas)