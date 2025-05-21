numeros = []

for n in range(10):
    numero = int(input(f"Digite um número inteiro: "))
    numeros.append(numero)  
numeros.sort()

print("Numeros em ordem crescente:")
for numero in numeros:
    print(numero)