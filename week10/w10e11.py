n = int(input("Tamanho dos vetores: "))
A = []
B = []
C = []
for i in range(n):
    A.append(int(input("A: ")))

for i in range(n):
    B.append(int(input("B: ")))

for i in range(n):
    C.append(A[i] + B[i])
print("Vetor C:", C)
