matriz = []

for linha in range(4):
    nova_linha = []
    for coluna in range(4):
        valor = int(input("Digite 16 valores (1 por 1): "))
        nova_linha.append(valor)
    matriz.append(nova_linha)

for linha in matriz:
    print(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            linha_maior = linha
            coluna_maior = coluna

print("Maior valor:", maior)
print("Linha:", linha_maior)
print("Coluna:", coluna_maior)