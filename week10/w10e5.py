impares = []
pares = []
print("digite 10 numeros")
for contador in range(10):
    numero = int(input(f"Digite um numero: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Os pares sao: {pares}, os impares sao {impares}")