frase = input('digite um nome ou frase: ')
vogais = ''
for letras in frase:
    if not (letras in "aeiouAEIOU"):
        vogais += letras
print(vogais)

