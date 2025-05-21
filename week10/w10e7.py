soma_numeros = 0
for numero in range (1,51):
    if numero % 2 == 0:
        soma_numeros += numero
print(f"A soma dos 50 primeiros numeros pares e: {soma_numeros}")