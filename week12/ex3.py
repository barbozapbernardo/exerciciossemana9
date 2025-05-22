alunos = []

for linha in range(5):
    matricula = int(input("Digite o numero de matricula: "))
    media_provas = int(input("Digite a media das provas: "))
    media_trabalhos = int(input("Digite a media dos trabalhos: "))
    nota_final = media_provas + media_trabalhos
    aluno = [matricula, media_provas, media_trabalhos, nota_final]
    alunos.append(aluno)

maior_nota = alunos[0][3]
matricula_maior = alunos[0][0]

for linha in range(5):
    if alunos[linha][3] > maior_nota:
        maior_nota = alunos[linha][3]
        matricula_maior = alunos[linha][0]

print("A matricula de quem tirou a maior media foi:", matricula_maior)