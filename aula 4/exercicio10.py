valores = [0]*5
i = 0
soma = 0
while i < 5:
    valores[i] = float(input(f"Digite o {i+1}º valor: "))
    soma = soma + valores[i]
    i = i + 1

maior = valores[0]
menor = valores[0]
i = 1
while i < 5:
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
    i = i + 1

media = soma / 5
print("Valores lidos:", valores)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média dos valores:", media)
