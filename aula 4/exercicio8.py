notas = [0]*15
i = 0
soma = 0
while i < 15:
    notas[i] = float(input(f"Digite a nota do aluno {i+1}: "))
    soma = soma + notas[i]
    i = i + 1

media = soma / 15
print("Média geral:", media)
