idades = int(input("digite quantas idades voce quer somar: "))
soma_idades = 0
for contador in range(idades):
    idade = int(input(f"Digite a {contador+1}a idade: "))
    soma_idades += idade
media = soma_idades / idades
print(f"A media das idades é: {media}")
