import random
numerosJogador1 = []
numerosJogador2 = []
soma1 = 0
soma2 = 0

for contador in range (3):
    numerosJogador1.append(random.randint(1,6))
    numerosJogador2.append(random.randint(1,6))

print(f"Os dados para o jogador 1 sao: {numerosJogador1}")
print(f"Os dados para o jogador 2 sao: {numerosJogador2}")

print (sum(numerosJogador1))
print (sum(numerosJogador2))

if sum(numerosJogador1) > sum(numerosJogador2):
    print("O jogador 1 venceu")
elif sum(numerosJogador1) == sum(numerosJogador2):
    print("A soma dos dados tem o mesmo valor. EMPATE")
else:
    print("O jogador 2 venceu") 