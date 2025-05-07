vetor = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 8:
    vetor[i] = float(input(f"Digite o {i+1}º número: "))
    i = i + 1
X = int(input("Digite a posição X (0 a 7): "))
Y = int(input("Digite a posição Y (0 a 7): "))
if 0 <= X < 8 and 0 <= Y < 8:
    soma = vetor[X] + vetor[Y]
    print(f"A soma dos valores nas posições {X} e {Y} é: {soma}")
else:
    print("Erro: posições inválidas. Digite valores entre 0 e 7.")
