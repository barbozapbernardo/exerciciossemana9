lista = []
for contador in range (5):
    valores = int(input("digite um valor inteiro: "))
    lista.append(valores)
print(lista)
print(sorted(lista))
print(list(reversed(lista)))
print(len(lista))
print(min(lista))
print(max(lista))
print(sum(lista))