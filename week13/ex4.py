def contar_letra(frase, letra_busca):
    quantidade = 0
    for caractere in frase:
        if caractere == letra_busca:
            quantidade += 1
    return quantidade

texto = input("Digite uma palavra ou frase: ")
letra = input("Digite a letra que deseja contar: ")

print(f"A letra '{letra}' aparece {contar_letra(texto, letra)} vezes.")
