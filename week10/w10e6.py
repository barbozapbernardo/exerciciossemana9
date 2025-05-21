dentro = []
fora = []
print("digite 10 numeros para saber quais estao entre 10 e 20")
for contador in range(10):
    numero = int(input(f"Digite um numero: "))
    if numero in range(10,20):
        dentro.append(numero)
    else:
        fora.append(numero)
print(f"Os numeros entre 10 e 20 sao: {dentro}, os demais numeros sao {fora}")