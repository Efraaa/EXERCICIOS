# Programa: Contagem de palavras em arquivo texto (ignorando pontuação e números)
# Feito por: Efraim
# Data de Criação: 07/06

arquivo = open("texto.txt", "r", encoding="utf-8")
texto = arquivo.read()
arquivo.close()
# Remove pontuação e números, mantém só letras e espaços, tudo em minúsculas
texto_limpo = ""
for char in texto:
    if char.isalpha() or char == " ":  # Remove pontuações e números, mantendo apenas letras e espaços, e converte tudo para minúsculas
        texto_limpo += char.lower()

palavras = texto_limpo.split()

palavras_unicas = []
contagens = []

for palavra in palavras:
    if palavra in palavras_unicas:
        posicao = palavras_unicas.index(palavra)
        contagens[posicao] += 1 # Incrementa contagem para palavra já vista
    else:
        palavras_unicas.append(palavra)
        contagens.append(1)

print("Contagem de palavras:")
for i in range(len(palavras_unicas)):
    print(f"{palavras_unicas[i]}: {contagens[i]}")