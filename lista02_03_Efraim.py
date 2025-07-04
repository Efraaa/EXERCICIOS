# Programa: Contagem de vogais, espaços e outros caracteres em frase
# Feito por: Efraim
# Data de Criação:07/06

frase = input('Digite sua frase').upper()
vogais = ['A','E','I','O','U']
resto = 0
q_espaços = 0
q_vogais = 0
for letra in frase:
    if letra in vogais:
        q_vogais += 1
    elif letra==" ":
        q_espaços += 1
        
resto = (len(frase)-(q_espaços+q_vogais))  #utilizei a lógica de fazer o tamanho da frase diminuido da quantidade de espaços com a de vogais
 
print(q_espaços)
print(q_vogais)
print(resto)
        