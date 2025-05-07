valores = [0]*5
i = 0
while i < 5:
    valores[i] = float(input(f"Digite o {i+1}º valor: "))
    i = i + 1

maior = valores[0]
menor = valores[0]
pos_maior = 0
pos_menor = 0
i = 1
while i < 5:
    if valores[i] > maior:
        maior = valores[i]
        pos_maior = i
    if valores[i] < menor:
        menor = valores[i]
        pos_menor = i
    i = i + 1

print("Posição do maior valor:", pos_maior)
print("Posição do menor valor:", pos_menor)
