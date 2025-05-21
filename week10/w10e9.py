texto = input("Digite um texto: ").lower()
vogais = ['a', 'e', 'i', 'o', 'u']
contagem = [0, 0, 0, 0, 0]

for letra in texto:
    for i in range(len(vogais)):
        if letra == vogais[i]:
            contagem[i] += 1

total = sum(contagem)

print("Total de vogais:", total)
for i in range(len(vogais)):
    if contagem[i] > 0:
        print(vogais[i], "=", contagem[i])
