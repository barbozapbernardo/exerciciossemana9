def encontrar_maior(lista):
    maior_valor = None
    for numero in lista:
        if (maior_valor is None) or (numero > maior_valor):
            maior_valor = numero
    return maior_valor

numeros = []

while True:
    valor = int(input("Digite um número inteiro: "))
    numeros.append(valor)
    opcao = input("Quer continuar adicionando? [S/N] ").strip().upper()
    if opcao == 'N':
        break

print("O maior número digitado foi:", encontrar_maior(numeros))
