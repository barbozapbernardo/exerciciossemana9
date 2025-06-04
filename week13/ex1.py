def somar_itens(lista):
    total = 0
    for item in lista:
        total += item
    return total

valores = []

while True:
    numero = int(input("Informe um número inteiro: "))
    valores.append(numero)
    continuar = input("Deseja adicionar mais um número? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("A soma dos números é:", somar_itens(valores))
