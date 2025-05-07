vetor = []
vetor_quadrados = []
i = 0
while i < 10:
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    vetor_quadrados.append(numero ** 2)
    i = i + 1
print("Vetor original:", vetor)
print("Vetor com os quadrados:", vetor_quadrados)
