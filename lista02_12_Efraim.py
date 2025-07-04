# Programa: Troca de letras maiúsculas por minúsculas em arquivo de texto
# Feito por: Efraim
# Data de Criação: 06/07

arquivo_entrada = open("entrada.txt", "r", encoding="utf-8")
texto = arquivo_entrada.read()
arquivo_entrada.close()

texto_convertido = ""
for char in texto:
    if char.islower():
        texto_convertido += char.upper()
    elif char.isupper():
        texto_convertido += char.lower() # Inverte a caixa das letras: minúsculas viram maiúsculas e vice-versa
    else:
        texto_convertido += char

arquivo_saida = open("saida.txt", "w", encoding="utf-8")
arquivo_saida.write(texto_convertido)
arquivo_saida.close()