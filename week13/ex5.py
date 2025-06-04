def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

while True:
    print("\nCALCULADORA")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
    opcao = int(input("Escolha a operação: "))
    
    if opcao == 0:
        break
    
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    if opcao == 1:
        print("Resultado:", somar(n1, n2))
    elif opcao == 2:
        print("Resultado:", subtrair(n1, n2))
    elif opcao == 3:
        print("Resultado:", multiplicar(n1, n2))
    elif opcao == 4:
        print("Resultado:", dividir(n1, n2))
    else:
        print("Opção inválida.")
