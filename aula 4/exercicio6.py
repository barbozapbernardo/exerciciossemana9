vetor = [0]*10
i = 0
while i < 10:
    vetor[i] = int(input(f"Digite o {i+1}º número: "))
    i = i + 1

maior = vetor[0]
menor = vetor[0]
i = 1
while i < 10:
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
    i = i + 1

print("Maior elemento:", maior)
print("Menor elemento:", menor)
