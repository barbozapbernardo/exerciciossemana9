numero = int(input("digite um numero entre 1 e 10: "))
print(f"\nTabuada do {numero}:")
for i in range(1,11):
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")
