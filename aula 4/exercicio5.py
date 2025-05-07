i = 0
quantidade_pares = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        quantidade_pares = quantidade_pares + 1

    i = i + 1

print("Quantidade de valores pares:", quantidade_pares)
