# Programa: Conversão de 50 temperaturas Celsius para Fahrenheit e análise de média
# Feito por: Efraim
# Data de Criação:  7/06

grauscelcius = []
grausf= []

for i  in range(2):
    t = int(input('Digite a temperatura'))
    grauscelcius.append(t)
 
for j in grauscelcius:
    grauf = ((j*1.8)+32)  #converte celcius para fahrenheit
    grausf.append(grauf)
    
somacelcius = 0
for i in grauscelcius:
    somacelcius += i
mediacelcius = somacelcius /len(grauscelcius)

somaf = 0 
for i in grausf:
    somaf += i
mediaf = somaf/ len(grausf)
    
maior_que_media = 0  #usado na contagem de numeros maiores que a média em fahrenheit
for i in grausf:
    if i > mediaf:
        maior_que_media += 1


print(grauf)
print(mediacelcius)
print(mediaf)
print(grauscelcius)
print(grausf)
     