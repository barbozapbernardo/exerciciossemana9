vetor = [0]*10
i = 0
negativos = 0
soma_positivos = 0
while i < 10:
    vetor[i] = float(input(f"Digite o {i+1}º número: "))
    if vetor[i] < 0:
        negativos = negativos + 1
    else:
        soma_positivos = soma_positivos + vetor[i]
    i = i + 1

print("Quantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)
