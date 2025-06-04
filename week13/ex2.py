def verificar_palindromo(texto):
    if texto == texto[::-1]:
        return 'Sim'
    else:
        return 'Não'

entrada = input('Digite uma palavra para verificar se é palíndromo: ')

print(verificar_palindromo(entrada))
